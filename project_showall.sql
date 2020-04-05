-- connection to the project database
\c project

\echo Table 1: Output from the ADDON table
SELECT * FROM Addon;

\echo Table 2: Output from the AMENITY table
SELECT * FROM Amenity;

\echo Table 3: Output from the BANKACCOUNT table
SELECT * FROM BankAccount;

\echo Table 4: Output from the BOOKABLE table
SELECT * FROM Bookable;

\echo Table 5: Output from the BOOKABLETYPE table
SELECT * FROM BookableType;

\echo Table 6: Output from the CREDITCARD table
SELECT * FROM CreditCard;

\echo Table 7: Output from the EXPERIENCE table
SELECT * FROM Experience;

\echo Table 8: Output from the EXPERIENCECATEGORY table
SELECT * FROM ExperienceCategory;

\echo Table 9: Output from the EXPERIENCEDATEPRICE table
SELECT * FROM ExperienceDatePrice;

\echo Table 10: Output from the GUEST table
SELECT * FROM Guest;

\echo Table 11: Output from the GUESTREVIEW table
SELECT * FROM GuestReview;

\echo Table 12: Output from the HOST table
SELECT * FROM Host;

\echo Table 13: Output from the HOSTREVIEW table
SELECT * FROM HostReview;

\echo Table 14: Output from the MESSAGE table
SELECT * FROM Message;

\echo Table 15: Output from the PAYMENT table
SELECT * FROM Payment;

\echo Table 16: Output from the PAYMENTOPTION table
SELECT * FROM PaymentOption;

\echo Table 17: Output from the PAYMENTOPTIONTYPE table
SELECT * FROM PaymentOptionType;

\echo Table 18: Output from the PAYOUT table
SELECT * FROM Payout;

\echo Table 19: Output from the RESERVATION table
SELECT * FROM Reservation;

\echo Table 20: Output from the RESERVATION_ADDONS table
SELECT * FROM Reservation_Addons;

\echo Table 21: Output from the STAY table
SELECT * FROM Stay;

\echo Table 22: Output from the STAYCATEGORY table
SELECT * FROM StayCategory;

\echo Table 23: Output from the STAYDATEPRICE table
SELECT * FROM StayDatePrice;

\echo Table 24: Output from the STAYHASAMENITY table
SELECT * FROM StayHasAmenity;

\echo Table 25: Output from the USER table
SELECT * FROM "User";
