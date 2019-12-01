--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 12.0

-- Started on 2019-12-02 01:12:17

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3146 (class 0 OID 18222)
-- Dependencies: 251
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public."User" (username, first_name, last_name, email, password, date_of_birth, phone_number, address) VALUES ('demoguest', 'Gabriel', 'Guest', 'gabrielguest@gmail.com', 'password', '1995-02-02', '4123334444', '2 Guest Gurney Georgia USA');
INSERT INTO public."User" (username, first_name, last_name, email, password, date_of_birth, phone_number, address) VALUES ('demohost', 'Henry', 'Host', 'henryhost@gmail.com', 'password', '1990-08-02', '4126667777', '8 Host Hills Handen USA');


--
-- TOC entry 3100 (class 0 OID 18002)
-- Dependencies: 205
-- Data for Name: bookabletype; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.bookabletype (bookable_type) VALUES ('stay');
INSERT INTO public.bookabletype (bookable_type) VALUES ('experience');


--
-- TOC entry 3114 (class 0 OID 18076)
-- Dependencies: 219
-- Data for Name: host; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.host (username, verified) VALUES ('demohost', true);


--
-- TOC entry 3099 (class 0 OID 17993)
-- Dependencies: 204
-- Data for Name: bookable; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.bookable (bookable_id, city, host_username, bookable_type) VALUES (1, 'Pittsburgh', 'demohost', 'stay');
INSERT INTO public.bookable (bookable_id, city, host_username, bookable_type) VALUES (2, 'Singapore', 'demohost', 'experience');


--
-- TOC entry 3093 (class 0 OID 17959)
-- Dependencies: 198
-- Data for Name: addon; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.addon (addon_id, name, price, bookable_id) VALUES (1, 'Packed Lunch', '$10.00', 2);
INSERT INTO public.addon (addon_id, name, price, bookable_id) VALUES (2, 'Pickup/Dropoff Downtown', '$20.00', 2);
INSERT INTO public.addon (addon_id, name, price, bookable_id) VALUES (3, 'Fresh Towels', '$5.00', 1);
INSERT INTO public.addon (addon_id, name, price, bookable_id) VALUES (4, 'Breakfast', '$10.00', 1);


--
-- TOC entry 3095 (class 0 OID 17971)
-- Dependencies: 200
-- Data for Name: amenity; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.amenity (amenity_id, name) VALUES (1, 'Kitchen');
INSERT INTO public.amenity (amenity_id, name) VALUES (2, 'Oven');
INSERT INTO public.amenity (amenity_id, name) VALUES (3, 'Washer');
INSERT INTO public.amenity (amenity_id, name) VALUES (4, 'Dryer');
INSERT INTO public.amenity (amenity_id, name) VALUES (5, 'Pool');


--
-- TOC entry 3125 (class 0 OID 18131)
-- Dependencies: 230
-- Data for Name: paymentoptiontype; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.paymentoptiontype (paymentoption_type) VALUES ('bankaccount');
INSERT INTO public.paymentoptiontype (paymentoption_type) VALUES ('creditcard');


--
-- TOC entry 3124 (class 0 OID 18122)
-- Dependencies: 229
-- Data for Name: paymentoption; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.paymentoption (paymentoption_id, billing_name, billing_address, billing_postalcode, username, paymentoption_type) VALUES (1, 'Henry Host', 'Henry Host''s Address Hostville USA', '82091', 'demohost', 'bankaccount');
INSERT INTO public.paymentoption (paymentoption_id, billing_name, billing_address, billing_postalcode, username, paymentoption_type) VALUES (2, 'Gabriel Guest', 'Gabriel Guest''s Address Guesttown USA', '12192', 'demoguest', 'creditcard');


--
-- TOC entry 3097 (class 0 OID 17982)
-- Dependencies: 202
-- Data for Name: bankaccount; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.bankaccount (paymentoption_id, account_type, routing_number, account_number) VALUES (1, 'checking', '011400071', '1298375911');


--
-- TOC entry 3102 (class 0 OID 18012)
-- Dependencies: 207
-- Data for Name: creditcard; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.creditcard (paymentoption_id, name_on_card, card_number, card_expiration, card_cvv) VALUES (1, 'Gabriel Guest', '6011000990139424', '12/12/2024', '090');


--
-- TOC entry 3107 (class 0 OID 18037)
-- Dependencies: 212
-- Data for Name: experiencecategory; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.experiencecategory (experience_category_id, name) VALUES (1, 'outdoor');
INSERT INTO public.experiencecategory (experience_category_id, name) VALUES (2, 'cooking');
INSERT INTO public.experiencecategory (experience_category_id, name) VALUES (3, 'art');


--
-- TOC entry 3105 (class 0 OID 18025)
-- Dependencies: 210
-- Data for Name: experience; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.experience (experience_bookable_id, name, duration, description, experience_category_id) VALUES (2, 'Walk the Treetops in Singapore', '04:00:00', 'In this half-day hike, we explore Singapore''s most famous nature reserves. Bring water and good shoes!', 1);


--
-- TOC entry 3109 (class 0 OID 18048)
-- Dependencies: 214
-- Data for Name: experiencedateprice; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.experiencedateprice (experience_bookable_id, date, price) VALUES (2, '2019-12-20', '$40.00');
INSERT INTO public.experiencedateprice (experience_bookable_id, date, price) VALUES (2, '2019-12-21', '$40.00');
INSERT INTO public.experiencedateprice (experience_bookable_id, date, price) VALUES (2, '2019-12-25', '$50.00');
INSERT INTO public.experiencedateprice (experience_bookable_id, date, price) VALUES (2, '1995-12-25', '$50.00');


--
-- TOC entry 3110 (class 0 OID 18054)
-- Dependencies: 215
-- Data for Name: guest; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.guest (username, banned) VALUES ('demoguest', false);


--
-- TOC entry 3132 (class 0 OID 18157)
-- Dependencies: 237
-- Data for Name: reservation; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.reservation (confirmation_id, confirmation_datetime, start_datetime, end_datetime, bookable_id, guest_username) VALUES (1, '2019-10-10 00:00:00', '2019-11-11 00:00:00', '2019-11-15 00:00:00', 1, 'demoguest');
INSERT INTO public.reservation (confirmation_id, confirmation_datetime, start_datetime, end_datetime, bookable_id, guest_username) VALUES (2, '2019-09-09 00:00:00', '2019-10-10 00:00:00', '2019-10-10 00:00:00', 2, 'demoguest');


--
-- TOC entry 3113 (class 0 OID 18066)
-- Dependencies: 218
-- Data for Name: guestreview; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.guestreview (guest_review_id, confirmation_id, guest_score, review_text, review_datetime) VALUES (1, 1, 5, 'Excellent guest, left place neat and tidy, will host again.', '2019-11-16 00:00:00');


--
-- TOC entry 3117 (class 0 OID 18088)
-- Dependencies: 222
-- Data for Name: hostreview; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.hostreview (host_review_id, confirmation_id, checkin_score, location_score, value_score, communication_score, accuracy_score, cleanliness_score, review_text, review_datetime) VALUES (1, 1, 5, 4, 5, 5, 4, 5, 'Nice charming place but older than expected. A little hard to get to other places without a car.', '2019-11-16 00:00:00');


--
-- TOC entry 3118 (class 0 OID 18098)
-- Dependencies: 223
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.message (sent_to, sent_by, message_text, datetime_sent, message_id) VALUES ('demohost', 'demoguest', 'Does your house have a pool?', '2019-02-02 00:00:00', 1);
INSERT INTO public.message (sent_to, sent_by, message_text, datetime_sent, message_id) VALUES ('demoguest', 'demohost', 'Yes it does, but it may have sharks.', '1995-02-03 00:00:00', 2);


--
-- TOC entry 3122 (class 0 OID 18112)
-- Dependencies: 227
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.payment (invoice_number, paymentoption_id, confirmation_id, amount, transaction_datetime) VALUES (1, 2, 1, '$240.00', '2019-10-10 00:00:00');
INSERT INTO public.payment (invoice_number, paymentoption_id, confirmation_id, amount, transaction_datetime) VALUES (2, 2, 2, '$40.00', '2019-09-09 00:00:00');


--
-- TOC entry 3129 (class 0 OID 18145)
-- Dependencies: 234
-- Data for Name: payout; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.payout (invoice_number, paymentoption_id, confirmation_id, amount, transaction_datetime) VALUES (1, 1, 1, '$240.00', '2019-11-16 00:00:00');
INSERT INTO public.payout (invoice_number, paymentoption_id, confirmation_id, amount, transaction_datetime) VALUES (2, 2, 2, '$80.00', '2019-10-11 00:00:00');


--
-- TOC entry 3135 (class 0 OID 18171)
-- Dependencies: 240
-- Data for Name: reservation_addons; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.reservation_addons (confirmation_id, addon_id) VALUES (1, 3);
INSERT INTO public.reservation_addons (confirmation_id, addon_id) VALUES (2, 2);


--
-- TOC entry 3140 (class 0 OID 18194)
-- Dependencies: 245
-- Data for Name: staycategory; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.staycategory (stay_category_id, name) VALUES (1, 'Apartment');
INSERT INTO public.staycategory (stay_category_id, name) VALUES (2, 'House');
INSERT INTO public.staycategory (stay_category_id, name) VALUES (3, 'Villa');
INSERT INTO public.staycategory (stay_category_id, name) VALUES (4, 'Trailer');


--
-- TOC entry 3138 (class 0 OID 18182)
-- Dependencies: 243
-- Data for Name: stay; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.stay (stay_bookable_id, name, stay_category_id, guest_num, bedrooms_num, beds_num, neighborhood, description) VALUES (1, 'Historic House in Pittsburgh', 2, 6, 3, 4, 'Oakland
', 'Traditionally built brick house with a pool and comfortable beds. Right in the middle of PGH and close to universities. ');


--
-- TOC entry 3142 (class 0 OID 18205)
-- Dependencies: 247
-- Data for Name: staydateprice; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.staydateprice (stay_bookable_id, date, price_per_night) VALUES (1, '2019-12-23', '$80.00');
INSERT INTO public.staydateprice (stay_bookable_id, date, price_per_night) VALUES (1, '2019-12-24', '$100.00');
INSERT INTO public.staydateprice (stay_bookable_id, date, price_per_night) VALUES (1, '2019-12-25', '$100.00');
INSERT INTO public.staydateprice (stay_bookable_id, date, price_per_night) VALUES (1, '2019-12-26', '$80.00');


--
-- TOC entry 3145 (class 0 OID 18215)
-- Dependencies: 250
-- Data for Name: stayhasamenity; Type: TABLE DATA; Schema: public; Owner: isdb
--

INSERT INTO public.stayhasamenity (stay_bookable_id, amenity_id) VALUES (1, 1);
INSERT INTO public.stayhasamenity (stay_bookable_id, amenity_id) VALUES (1, 3);
INSERT INTO public.stayhasamenity (stay_bookable_id, amenity_id) VALUES (1, 5);


--
-- TOC entry 3152 (class 0 OID 0)
-- Dependencies: 196
-- Name: addon_addon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.addon_addon_id_seq', 4, true);


--
-- TOC entry 3153 (class 0 OID 0)
-- Dependencies: 197
-- Name: addon_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.addon_bookable_id_seq', 1, false);


--
-- TOC entry 3154 (class 0 OID 0)
-- Dependencies: 199
-- Name: amenity_amenity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.amenity_amenity_id_seq', 5, true);


--
-- TOC entry 3155 (class 0 OID 0)
-- Dependencies: 201
-- Name: bankaccount_paymentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.bankaccount_paymentoption_id_seq', 1, true);


--
-- TOC entry 3156 (class 0 OID 0)
-- Dependencies: 203
-- Name: bookable_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.bookable_bookable_id_seq', 2, true);


--
-- TOC entry 3157 (class 0 OID 0)
-- Dependencies: 206
-- Name: creditcard_paymentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.creditcard_paymentoption_id_seq', 1, true);


--
-- TOC entry 3158 (class 0 OID 0)
-- Dependencies: 208
-- Name: experience_experience_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.experience_experience_bookable_id_seq', 1, false);


--
-- TOC entry 3159 (class 0 OID 0)
-- Dependencies: 209
-- Name: experience_experience_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.experience_experience_category_id_seq', 1, true);


--
-- TOC entry 3160 (class 0 OID 0)
-- Dependencies: 211
-- Name: experiencecategory_experience_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.experiencecategory_experience_category_id_seq', 3, true);


--
-- TOC entry 3161 (class 0 OID 0)
-- Dependencies: 213
-- Name: experiencedateprice_experience_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.experiencedateprice_experience_bookable_id_seq', 1, false);


--
-- TOC entry 3162 (class 0 OID 0)
-- Dependencies: 217
-- Name: guestreview_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.guestreview_confirmation_id_seq', 1, false);


--
-- TOC entry 3163 (class 0 OID 0)
-- Dependencies: 216
-- Name: guestreview_guest_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.guestreview_guest_review_id_seq', 1, true);


--
-- TOC entry 3164 (class 0 OID 0)
-- Dependencies: 221
-- Name: hostreview_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.hostreview_confirmation_id_seq', 1, false);


--
-- TOC entry 3165 (class 0 OID 0)
-- Dependencies: 220
-- Name: hostreview_host_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.hostreview_host_review_id_seq', 1, true);


--
-- TOC entry 3166 (class 0 OID 0)
-- Dependencies: 226
-- Name: payment_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payment_confirmation_id_seq', 1, false);


--
-- TOC entry 3167 (class 0 OID 0)
-- Dependencies: 224
-- Name: payment_invoice_number_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payment_invoice_number_seq', 2, true);


--
-- TOC entry 3168 (class 0 OID 0)
-- Dependencies: 225
-- Name: payment_paymentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payment_paymentoption_id_seq', 1, false);


--
-- TOC entry 3169 (class 0 OID 0)
-- Dependencies: 228
-- Name: paymentoption_paymentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.paymentoption_paymentoption_id_seq', 2, true);


--
-- TOC entry 3170 (class 0 OID 0)
-- Dependencies: 233
-- Name: payout_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payout_confirmation_id_seq', 1, false);


--
-- TOC entry 3171 (class 0 OID 0)
-- Dependencies: 231
-- Name: payout_invoice_number_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payout_invoice_number_seq', 2, true);


--
-- TOC entry 3172 (class 0 OID 0)
-- Dependencies: 232
-- Name: payout_paymentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.payout_paymentoption_id_seq', 1, false);


--
-- TOC entry 3173 (class 0 OID 0)
-- Dependencies: 239
-- Name: reservation_addons_addon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.reservation_addons_addon_id_seq', 1, false);


--
-- TOC entry 3174 (class 0 OID 0)
-- Dependencies: 238
-- Name: reservation_addons_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.reservation_addons_confirmation_id_seq', 1, false);


--
-- TOC entry 3175 (class 0 OID 0)
-- Dependencies: 236
-- Name: reservation_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.reservation_bookable_id_seq', 1, false);


--
-- TOC entry 3176 (class 0 OID 0)
-- Dependencies: 235
-- Name: reservation_confirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.reservation_confirmation_id_seq', 2, true);


--
-- TOC entry 3177 (class 0 OID 0)
-- Dependencies: 241
-- Name: stay_stay_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.stay_stay_bookable_id_seq', 1, false);


--
-- TOC entry 3178 (class 0 OID 0)
-- Dependencies: 242
-- Name: stay_stay_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.stay_stay_category_id_seq', 1, false);


--
-- TOC entry 3179 (class 0 OID 0)
-- Dependencies: 244
-- Name: staycategory_stay_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.staycategory_stay_category_id_seq', 4, true);


--
-- TOC entry 3180 (class 0 OID 0)
-- Dependencies: 246
-- Name: staydateprice_stay_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.staydateprice_stay_bookable_id_seq', 1, false);


--
-- TOC entry 3181 (class 0 OID 0)
-- Dependencies: 249
-- Name: stayhasamenity_amenity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.stayhasamenity_amenity_id_seq', 1, false);


--
-- TOC entry 3182 (class 0 OID 0)
-- Dependencies: 248
-- Name: stayhasamenity_stay_bookable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: isdb
--

SELECT pg_catalog.setval('public.stayhasamenity_stay_bookable_id_seq', 1, false);


-- Completed on 2019-12-02 01:12:18

--
-- PostgreSQL database dump complete
--

