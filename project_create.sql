-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-11-30 18:23:44.855

-- tables
-- Table: Addon
CREATE TABLE Addon (
    addon_id serial  NOT NULL,
    name text  NOT NULL,
    price money  NOT NULL,
    bookable_id serial  NOT NULL,
    CONSTRAINT Addon_pk PRIMARY KEY (addon_id)
);

-- Table: Amenity
CREATE TABLE Amenity (
    amenity_id serial  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Amenity_pk PRIMARY KEY (amenity_id)
);

-- Table: BankAccount
CREATE TABLE BankAccount (
    paymentoption_id serial  NOT NULL,
    account_type text  NOT NULL,
    routing_number text  NOT NULL,
    account_number text  NOT NULL,
    CONSTRAINT BankAccount_pk PRIMARY KEY (paymentoption_id)
);

-- Table: Bookable
CREATE TABLE Bookable (
    bookable_id serial  NOT NULL,
    city text  NOT NULL,
    host_username text  NOT NULL,
    bookable_type text  NOT NULL,
    CONSTRAINT Bookable_pk PRIMARY KEY (bookable_id)
);

-- Table: BookableType
CREATE TABLE BookableType (
    bookable_type text  NOT NULL,
    CONSTRAINT BookableType_pk PRIMARY KEY (bookable_type)
);

-- Table: CreditCard
CREATE TABLE CreditCard (
    paymentoption_id serial  NOT NULL,
    name_on_card text  NOT NULL,
    card_number text  NOT NULL,
    card_expiration text  NOT NULL,
    card_cvv text  NOT NULL,
    CONSTRAINT CreditCard_pk PRIMARY KEY (paymentoption_id)
);

-- Table: Experience
CREATE TABLE Experience (
    experience_bookable_id serial  NOT NULL,
    name text  NOT NULL,
    duration interval  NOT NULL,
    description text  NOT NULL,
    experience_category_id serial  NOT NULL,
    CONSTRAINT Experience_pk PRIMARY KEY (experience_bookable_id)
);

-- Table: ExperienceCategory
CREATE TABLE ExperienceCategory (
    experience_category_id serial  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT ExperienceCategory_pk PRIMARY KEY (experience_category_id)
);

-- Table: ExperienceDatePrice
CREATE TABLE ExperienceDatePrice (
    experience_bookable_id serial  NOT NULL,
    date date  NOT NULL,
    price money  NOT NULL,
    CONSTRAINT ExperienceDatePrice_pk PRIMARY KEY (experience_bookable_id,date)
);

-- Table: Guest
CREATE TABLE Guest (
    username text  NOT NULL,
    banned boolean  NOT NULL,
    CONSTRAINT Guest_pk PRIMARY KEY (username)
);

-- Table: GuestReview
CREATE TABLE GuestReview (
    guest_review_id serial  NOT NULL,
    confirmation_id serial  NOT NULL,
    guest_score int  NOT NULL,
    review_text text  NOT NULL,
    review_datetime timestamp  NOT NULL,
    CONSTRAINT GuestReview_pk PRIMARY KEY (guest_review_id)
);

-- Table: Host
CREATE TABLE Host (
    username text  NOT NULL,
    verified boolean  NOT NULL,
    CONSTRAINT Host_pk PRIMARY KEY (username)
);

-- Table: HostReview
CREATE TABLE HostReview (
    host_review_id serial  NOT NULL,
    confirmation_id serial  NOT NULL,
    checkin_score int  NOT NULL,
    location_score int  NOT NULL,
    value_score int  NOT NULL,
    communication_score int  NOT NULL,
    accuracy_score int  NOT NULL,
    cleanliness_score int  NOT NULL,
    review_text text  NOT NULL,
    review_datetime timestamp  NOT NULL,
    CONSTRAINT HostReview_pk PRIMARY KEY (host_review_id)
);

-- Table: Message
CREATE TABLE Message (
    message_id serial  NOT NULL,
    sent_to text  NOT NULL,
    sent_by text  NOT NULL,
    message_text text  NOT NULL,
    datetime_sent timestamp  NOT NULL,
    CONSTRAINT Message_pk PRIMARY KEY (message_id)
);

-- Table: Payment
CREATE TABLE Payment (
    invoice_number serial  NOT NULL,
    paymentoption_id serial  NOT NULL,
    confirmation_id serial  NOT NULL,
    amount money  NOT NULL,
    transaction_datetime timestamp  NOT NULL,
    CONSTRAINT Payment_pk PRIMARY KEY (invoice_number)
);

-- Table: PaymentOption
CREATE TABLE PaymentOption (
    paymentoption_id serial  NOT NULL,
    billing_name text  NOT NULL,
    billing_address text  NOT NULL,
    billing_postalcode text  NOT NULL,
    username text  NOT NULL,
    paymentoption_type text  NOT NULL,
    CONSTRAINT PaymentOption_pk PRIMARY KEY (paymentoption_id)
);

-- Table: PaymentOptionType
CREATE TABLE PaymentOptionType (
    paymentoption_type text  NOT NULL,
    CONSTRAINT PaymentOptionType_pk PRIMARY KEY (paymentoption_type)
);

-- Table: Payout
CREATE TABLE Payout (
    invoice_number serial  NOT NULL,
    paymentoption_id serial  NOT NULL,
    confirmation_id serial  NOT NULL,
    amount money  NOT NULL,
    transaction_datetime timestamp  NOT NULL,
    CONSTRAINT Payout_pk PRIMARY KEY (invoice_number)
);

-- Table: Reservation
CREATE TABLE Reservation (
    confirmation_id serial  NOT NULL,
    confirmation_datetime timestamp  NOT NULL,
    start_datetime timestamp  NOT NULL,
    end_datetime timestamp  NOT NULL,
    bookable_id serial  NOT NULL,
    guest_username text  NOT NULL,
    CONSTRAINT Reservation_pk PRIMARY KEY (confirmation_id)
);

-- Table: Reservation_Addons
CREATE TABLE Reservation_Addons (
    confirmation_id serial  NOT NULL,
    addon_id serial  NOT NULL,
    CONSTRAINT Reservation_Addons_pk PRIMARY KEY (confirmation_id,addon_id)
);

-- Table: Stay
CREATE TABLE Stay (
    stay_bookable_id serial  NOT NULL,
    name text  NOT NULL,
    stay_category_id serial  NOT NULL,
    guest_num int  NOT NULL,
    bedrooms_num int  NOT NULL,
    beds_num int  NOT NULL,
    neighborhood text  NOT NULL,
    description text  NOT NULL,
    CONSTRAINT Stay_pk PRIMARY KEY (stay_bookable_id)
);

-- Table: StayCategory
CREATE TABLE StayCategory (
    stay_category_id serial  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT StayCategory_pk PRIMARY KEY (stay_category_id)
);

-- Table: StayDatePrice
CREATE TABLE StayDatePrice (
    stay_bookable_id serial  NOT NULL,
    date date  NOT NULL,
    price_per_night money  NOT NULL,
    CONSTRAINT StayDatePrice_pk PRIMARY KEY (stay_bookable_id,date)
);

-- Table: StayHasAmenity
CREATE TABLE StayHasAmenity (
    stay_bookable_id serial  NOT NULL,
    amenity_id serial  NOT NULL,
    CONSTRAINT StayHasAmenity_pk PRIMARY KEY (stay_bookable_id,amenity_id)
);

-- Table: User
CREATE TABLE "User" (
    username text  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    email text  NOT NULL,
    password text  NOT NULL,
    date_of_birth date  NOT NULL,
    phone_number text  NOT NULL,
    address text  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (username)
);

-- foreign keys
-- Reference: BankAccount_PaymentOption (table: BankAccount)
ALTER TABLE BankAccount ADD CONSTRAINT BankAccount_PaymentOption
    FOREIGN KEY (paymentoption_id)
    REFERENCES PaymentOption (paymentoption_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: BookableType_Bookable (table: Bookable)
ALTER TABLE Bookable ADD CONSTRAINT BookableType_Bookable
    FOREIGN KEY (bookable_type)
    REFERENCES BookableType (bookable_type)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bookable_Addon (table: Addon)
ALTER TABLE Addon ADD CONSTRAINT Bookable_Addon
    FOREIGN KEY (bookable_id)
    REFERENCES Bookable (bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bookable_Experience (table: Experience)
ALTER TABLE Experience ADD CONSTRAINT Bookable_Experience
    FOREIGN KEY (experience_bookable_id)
    REFERENCES Bookable (bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bookable_Host (table: Bookable)
ALTER TABLE Bookable ADD CONSTRAINT Bookable_Host
    FOREIGN KEY (host_username)
    REFERENCES Host (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bookable_Stay (table: Stay)
ALTER TABLE Stay ADD CONSTRAINT Bookable_Stay
    FOREIGN KEY (stay_bookable_id)
    REFERENCES Bookable (bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: CreditCard_PaymentOption (table: CreditCard)
ALTER TABLE CreditCard ADD CONSTRAINT CreditCard_PaymentOption
    FOREIGN KEY (paymentoption_id)
    REFERENCES PaymentOption (paymentoption_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Experience_ExperienceCategory (table: Experience)
ALTER TABLE Experience ADD CONSTRAINT Experience_ExperienceCategory
    FOREIGN KEY (experience_category_id)
    REFERENCES ExperienceCategory (experience_category_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Experience_ExperienceDatePrice (table: ExperienceDatePrice)
ALTER TABLE ExperienceDatePrice ADD CONSTRAINT Experience_ExperienceDatePrice
    FOREIGN KEY (experience_bookable_id)
    REFERENCES Experience (experience_bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: GuestReview_Reservation (table: GuestReview)
ALTER TABLE GuestReview ADD CONSTRAINT GuestReview_Reservation
    FOREIGN KEY (confirmation_id)
    REFERENCES Reservation (confirmation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guest_User (table: Guest)
ALTER TABLE Guest ADD CONSTRAINT Guest_User
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: HostReview_Reservation (table: HostReview)
ALTER TABLE HostReview ADD CONSTRAINT HostReview_Reservation
    FOREIGN KEY (confirmation_id)
    REFERENCES Reservation (confirmation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Host_User (table: Host)
ALTER TABLE Host ADD CONSTRAINT Host_User
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Message_User_Receiver (table: Message)
ALTER TABLE Message ADD CONSTRAINT Message_User_Receiver
    FOREIGN KEY (sent_to)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Message_User_Sender (table: Message)
ALTER TABLE Message ADD CONSTRAINT Message_User_Sender
    FOREIGN KEY (sent_by)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: PaymentOptionType_PaymentOption (table: PaymentOption)
ALTER TABLE PaymentOption ADD CONSTRAINT PaymentOptionType_PaymentOption
    FOREIGN KEY (paymentoption_type)
    REFERENCES PaymentOptionType (paymentoption_type)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: PaymentOption_User (table: PaymentOption)
ALTER TABLE PaymentOption ADD CONSTRAINT PaymentOption_User
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Payment_PaymentOption (table: Payment)
ALTER TABLE Payment ADD CONSTRAINT Payment_PaymentOption
    FOREIGN KEY (paymentoption_id)
    REFERENCES PaymentOption (paymentoption_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Payout_PaymentOption (table: Payout)
ALTER TABLE Payout ADD CONSTRAINT Payout_PaymentOption
    FOREIGN KEY (paymentoption_id)
    REFERENCES PaymentOption (paymentoption_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Addons_Addon (table: Reservation_Addons)
ALTER TABLE Reservation_Addons ADD CONSTRAINT Reservation_Addons_Addon
    FOREIGN KEY (addon_id)
    REFERENCES Addon (addon_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Addons_Reservation (table: Reservation_Addons)
ALTER TABLE Reservation_Addons ADD CONSTRAINT Reservation_Addons_Reservation
    FOREIGN KEY (confirmation_id)
    REFERENCES Reservation (confirmation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Bookable (table: Reservation)
ALTER TABLE Reservation ADD CONSTRAINT Reservation_Bookable
    FOREIGN KEY (bookable_id)
    REFERENCES Bookable (bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Guest (table: Reservation)
ALTER TABLE Reservation ADD CONSTRAINT Reservation_Guest
    FOREIGN KEY (guest_username)
    REFERENCES Guest (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Payment (table: Payment)
ALTER TABLE Payment ADD CONSTRAINT Reservation_Payment
    FOREIGN KEY (confirmation_id)
    REFERENCES Reservation (confirmation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservation_Payout (table: Payout)
ALTER TABLE Payout ADD CONSTRAINT Reservation_Payout
    FOREIGN KEY (confirmation_id)
    REFERENCES Reservation (confirmation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: StayDatePrice_Stay (table: StayDatePrice)
ALTER TABLE StayDatePrice ADD CONSTRAINT StayDatePrice_Stay
    FOREIGN KEY (stay_bookable_id)
    REFERENCES Stay (stay_bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: StayHasAmenity_Amenity (table: StayHasAmenity)
ALTER TABLE StayHasAmenity ADD CONSTRAINT StayHasAmenity_Amenity
    FOREIGN KEY (amenity_id)
    REFERENCES Amenity (amenity_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Stay_StayCategory (table: Stay)
ALTER TABLE Stay ADD CONSTRAINT Stay_StayCategory
    FOREIGN KEY (stay_category_id)
    REFERENCES StayCategory (stay_category_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Stay_StayHasAmenity (table: StayHasAmenity)
ALTER TABLE StayHasAmenity ADD CONSTRAINT Stay_StayHasAmenity
    FOREIGN KEY (stay_bookable_id)
    REFERENCES Stay (stay_bookable_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

