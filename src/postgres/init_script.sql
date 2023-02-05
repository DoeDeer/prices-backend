--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Debian 12.5-1.pgdg100+1)
-- Dumped by pg_dump version 12.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.customers (
    customer text
);


--
-- Name: ports; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ports (
    code text NOT NULL,
    name text NOT NULL
);


--
-- Name: prices; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.prices (
    orig_code text NOT NULL,
    dest_code text NOT NULL,
    day date NOT NULL,
    price integer NOT NULL,
    customer text
);


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.customers (customer) FROM stdin;
Acme Inc.
ООО Вектор
Næstad AS
\.


--
-- Data for Name: ports; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.ports (code, name) FROM stdin;
CNCWN	Chiwan
IESNN	Shannon
FRLVE	Le Verdon-sur-Mer
NOOSL	Oslo
GBPME	Portsmouth
NOSVG	Stavanger
FIHEL	Helsingfors (Helsinki)
NOMAY	Måløy
FRLIO	Lyon
SEHAD	Halmstad
GBTIL	Tilbury
DKCPH	Copenhagen (København)
NOFRK	Fredrikstad
CNYAT	Yantai
CNSNZ	Shenzhen
NOSKE	Skien
DEWVN	Wilhelmshaven
NOKSU	Kristiansund
SEMMA	Malmö
FIRAA	Brahestad (Raahe)
FRDKK	Dunkerque
GBLON	London
NOSVE	Svelgen
FRBAS	Bassens
NLMOE	Moerdijk
IEDUB	Dublin
FRDPE	Dieppe
FIKOK	Karleby (Kokkola)
NLRTM	Rotterdam
GBLTP	London Thamesport
BEZEE	Zeebrugge
FIOUL	Uleåborg (Oulu)
NOFUS	Fusa
FRNEG	Bougenais
DEBRE	Bremen
SENRK	Norrköping
RUKDT	Kronshtadt
FRLRH	La Rochelle
FIMTY	Mantyluoto
NOIKR	Ikornnes
DKFRC	Fredericia
NOHVI	Håvik
FRMTX	Montoir-de-Bretagne
FIKTK	Kotka
EEMUG	Muuga
PLSZZ	Szczecin
NOUME	Straume Industriområde
CNSHK	Shekou
GBTEE	Teesport
FRBOD	Bordeaux
FRLEH	Le Havre
HKHKG	Hong Kong
SESOE	Södertälje
NOHAL	Halden
ESGIJ	Gijón
NOBVG	Berlevåg
IEORK	Cork
DEBRV	Bremerhaven
ESZAZ	Zaragoza
SEWAL	Wallhamn
CNNBO	Ningbo
NOFRO	Florø
CNDAL	Dalian
GBMNC	Manchester
PLGDY	Gdynia
CNSGH	Shanghai
FITKU	Åbo (Turku)
GBHUL	Hull
ESVGO	Vigo
SEHEL	Helsingborg
NOMOL	Molde
NOTON	Tønsberg
CNHDG	Huadu Pt
BEANR	Antwerpen
FIRAU	Rauma (Raumo)
PLGDN	Gdansk
NODRM	Drammen
NOSAS	Sandnes
NOKRS	Kristiansand
NOSUN	Sunndalsøra
GBBEL	Belfast
DKAAR	Århus
FRURO	Rouen
GBLGP	London Gateway Port
SEAHU	Åhus
NOBVK	Brevik
FRANT	Antibes
RUARH	Arkhangelsk
NOTOS	Tromsø
SEGOT	Gothenburg (Göteborg)
FIIMA	Imatra
FIKEM	Kemi/Torneå (Kemi/Tornio)
GBGRG	Grangemouth
EETLL	Tallinn
FIHMN	Fredrikshamn (Hamina)
RULED	Saint Petersburg (ex Leningrad)
GBLIV	Liverpool
CNGGZ	Guangzhou
NOTRD	Trondheim
FRIRK	Dunkirk
FRNTE	Nantes
CNQIN	Qingdao
RULUG	Lugovoye
GBBRS	Bristol
GBGOO	Goole
CNLYG	Lianyungang
GBTHP	Thamesport
NOHAU	Haugesund
LVRIX	Riga
DKAAL	Aalborg
GBFXT	Felixstowe
NOMSS	Moss
NLAMS	Amsterdam
FOTHO	Thorshavn
NOHYR	Høyanger
NOTAE	Tananger
CNTXG	Xingang (Tianjin New Pt)
SEGVX	Gävle
GBSOU	Southampton
CNXAM	Xiamen
RUULU	Ust'-Luga
NOBGO	Bergen
ESMPG	Marin, Pontevedra
DEHAM	Hamburg
SEOXE	Oxelösund
NOLAR	Larvik
CNYTN	Yantian
ISREY	Reykjavík
ESBIO	Bilbao
ISGRT	Grundartangi
NOGJM	Gjemnes
FRBES	Brest
NOORK	Orkanger
NOAES	Ålesund
SESTO	Stockholm
GBIMM	Immingham
LTKLJ	Klaipeda
RUKGD	Kaliningrad
GBGRK	Greenock
SEPIT	Piteå
ESVIT	Vitoria-Gasteiz
DKEBJ	Esbjerg
GBSSH	South Shields
\.


--
-- Data for Name: prices; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.prices (orig_code, dest_code, day, price, customer) FROM stdin;
CNSGH	BEANR	2016-01-01	300	Acme Inc.
CNSGH	BEANR	2016-01-01	400	ООО Вектор
CNSGH	BEANR	2016-01-01	500	Næstad AS
CNSGH	BEZEE	2016-01-01	300	Acme Inc.
CNSGH	BEZEE	2016-01-01	400	ООО Вектор
CNSGH	BEZEE	2016-01-01	500	Næstad AS
CNSGH	DEBRV	2016-01-01	500	Acme Inc.
CNSGH	DEBRV	2016-01-01	600	ООО Вектор
CNSGH	DEBRV	2016-01-01	700	Næstad AS
CNSGH	DEHAM	2016-01-01	500	Acme Inc.
CNSGH	DEHAM	2016-01-01	600	ООО Вектор
CNSGH	DEHAM	2016-01-01	700	Næstad AS
CNSGH	FRLEH	2016-01-01	600	Acme Inc.
CNSGH	FRLEH	2016-01-01	700	ООО Вектор
CNSGH	FRLEH	2016-01-01	800	Næstad AS
CNSGH	NLRTM	2016-01-01	700	Acme Inc.
CNSGH	NLRTM	2016-01-01	800	ООО Вектор
CNSGH	NLRTM	2016-01-01	900	Næstad AS
CNSGH	BEANR	2016-01-02	300	Acme Inc.
CNSGH	BEANR	2016-01-02	400	ООО Вектор
CNSGH	BEANR	2016-01-02	500	Næstad AS
CNSGH	BEZEE	2016-01-02	300	Acme Inc.
CNSGH	BEZEE	2016-01-02	400	ООО Вектор
CNSGH	BEZEE	2016-01-02	500	Næstad AS
CNSGH	DEBRV	2016-01-02	500	Acme Inc.
CNSGH	DEBRV	2016-01-02	600	ООО Вектор
CNSGH	DEBRV	2016-01-02	700	Næstad AS
CNSGH	DEHAM	2016-01-02	500	Acme Inc.
CNSGH	DEHAM	2016-01-02	600	ООО Вектор
CNSGH	DEHAM	2016-01-02	700	Næstad AS
CNSGH	FRLEH	2016-01-02	600	Acme Inc.
CNSGH	FRLEH	2016-01-02	700	ООО Вектор
CNSGH	FRLEH	2016-01-02	800	Næstad AS
CNSGH	NLRTM	2016-01-02	700	Acme Inc.
CNSGH	NLRTM	2016-01-02	800	ООО Вектор
CNSGH	NLRTM	2016-01-02	900	Næstad AS
CNSGH	BEANR	2016-01-04	300	Acme Inc.
CNSGH	BEZEE	2016-01-04	300	Acme Inc.
CNSGH	DEBRV	2016-01-04	500	Acme Inc.
CNSGH	DEHAM	2016-01-04	500	Acme Inc.
CNSGH	FRLEH	2016-01-04	600	Acme Inc.
CNSGH	NLRTM	2016-01-04	700	Acme Inc.
CNSGH	BEANR	2016-01-05	300	Acme Inc.
CNSGH	BEANR	2016-01-05	400	ООО Вектор
CNSGH	BEANR	2016-01-05	500	Næstad AS
CNSGH	BEZEE	2016-01-05	300	Acme Inc.
CNSGH	BEZEE	2016-01-05	400	ООО Вектор
CNSGH	BEZEE	2016-01-05	500	Næstad AS
CNSGH	DEBRV	2016-01-05	500	Acme Inc.
CNSGH	DEBRV	2016-01-05	600	ООО Вектор
CNSGH	DEBRV	2016-01-05	700	Næstad AS
CNSGH	DEHAM	2016-01-05	500	Acme Inc.
CNSGH	DEHAM	2016-01-05	600	ООО Вектор
CNSGH	DEHAM	2016-01-05	700	Næstad AS
CNSGH	FRLEH	2016-01-05	600	Acme Inc.
CNSGH	FRLEH	2016-01-05	700	ООО Вектор
CNSGH	FRLEH	2016-01-05	800	Næstad AS
CNSGH	NLRTM	2016-01-05	700	Acme Inc.
\.


--
-- Name: ports ports_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ports
    ADD CONSTRAINT ports_pkey PRIMARY KEY (code);


--
-- Name: prices prices_dest_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.prices
    ADD CONSTRAINT prices_dest_code_fkey FOREIGN KEY (dest_code) REFERENCES public.ports(code);


--
-- Name: prices prices_orig_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.prices
    ADD CONSTRAINT prices_orig_code_fkey FOREIGN KEY (orig_code) REFERENCES public.ports(code);


--
-- PostgreSQL database dump complete
--
