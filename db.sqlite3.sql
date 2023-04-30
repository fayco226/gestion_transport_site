BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "account_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"profil_photo"	varchar(100),
	"role"	varchar(50),
	"phone"	varchar(128) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "account_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	bigint NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "account_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "account_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	bigint NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "account_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	bigint NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "account_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "transport_car" (
	"id"	integer NOT NULL,
	"nom"	varchar(50) NOT NULL,
	"nombre_de_places"	integer NOT NULL,
	"capacite_bagage"	integer NOT NULL,
	"nombre_de_car"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_voyages" (
	"id"	integer NOT NULL,
	"ville_depart"	varchar(200) NOT NULL,
	"ville_arrive"	varchar(200) NOT NULL,
	"heure_depart"	time NOT NULL,
	"place_number"	integer NOT NULL,
	"prix"	integer NOT NULL,
	"car_id"	bigint NOT NULL,
	FOREIGN KEY("car_id") REFERENCES "transport_car"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_voyage_programmer" (
	"id"	integer NOT NULL,
	"ville_depart"	varchar(200) NOT NULL,
	"ville_arrive"	varchar(200) NOT NULL,
	"heure_depart"	time NOT NULL,
	"prix"	integer NOT NULL,
	"car_id"	bigint NOT NULL,
	FOREIGN KEY("car_id") REFERENCES "transport_car"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_place" (
	"id"	integer NOT NULL,
	"date"	date NOT NULL,
	"voyage_id"	bigint NOT NULL,
	"disponibilite"	bool NOT NULL,
	"nombre_de_place_restant"	integer NOT NULL,
	FOREIGN KEY("voyage_id") REFERENCES "transport_voyages"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_ville" (
	"id"	integer NOT NULL,
	"nom"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_client" (
	"id"	integer NOT NULL,
	"nom"	varchar(50) NOT NULL,
	"prenom"	varchar(100) NOT NULL,
	"addresse"	varchar(100) NOT NULL,
	"cnib"	integer NOT NULL,
	"email"	varchar(254) NOT NULL,
	"telephone"	varchar(128) NOT NULL,
	"motDePass"	varchar(50) NOT NULL,
	"nomUtisateur"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_reserve" (
	"id"	integer NOT NULL,
	"villeDepart"	varchar(50) NOT NULL,
	"villeArrive"	varchar(50) NOT NULL,
	"nombreDePlace"	integer NOT NULL,
	"typeVoyage"	varchar(50) NOT NULL,
	"dateReservation"	date NOT NULL,
	"NomEtPrenom"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_courier" (
	"id"	integer NOT NULL,
	"objetAEnvoyer"	varchar(50) NOT NULL,
	"prixDeLobjet"	integer NOT NULL,
	"telephone"	varchar(50) NOT NULL,
	"nomEtPrenomDeExpediteur"	varchar(50) NOT NULL,
	"nomEtPrenomDuDestinatair"	varchar(100) NOT NULL,
	"cnib"	integer NOT NULL,
	"validerArrive"	bool NOT NULL,
	"validerPris"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "transport_reservation" (
	"id"	integer NOT NULL,
	"date"	date NOT NULL,
	"client_id"	bigint NOT NULL,
	"voyage_id"	bigint NOT NULL,
	"valider_reservation"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("client_id") REFERENCES "transport_client"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("voyage_id") REFERENCES "transport_voyages"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2023-02-15 00:59:35.462166'),
 (2,'contenttypes','0002_remove_content_type_name','2023-02-15 00:59:35.617399'),
 (3,'auth','0001_initial','2023-02-15 00:59:35.853554'),
 (4,'auth','0002_alter_permission_name_max_length','2023-02-15 00:59:35.920502'),
 (5,'auth','0003_alter_user_email_max_length','2023-02-15 00:59:36.101728'),
 (6,'auth','0004_alter_user_username_opts','2023-02-15 00:59:36.209022'),
 (7,'auth','0005_alter_user_last_login_null','2023-02-15 00:59:36.337565'),
 (8,'auth','0006_require_contenttypes_0002','2023-02-15 00:59:36.927725'),
 (9,'auth','0007_alter_validators_add_error_messages','2023-02-15 00:59:37.782910'),
 (10,'auth','0008_alter_user_username_max_length','2023-02-15 00:59:38.049531'),
 (11,'auth','0009_alter_user_last_name_max_length','2023-02-15 00:59:38.195440'),
 (12,'auth','0010_alter_group_name_max_length','2023-02-15 00:59:38.356226'),
 (13,'auth','0011_update_proxy_permissions','2023-02-15 00:59:38.607087'),
 (14,'auth','0012_alter_user_first_name_max_length','2023-02-15 00:59:38.733718'),
 (15,'account','0001_initial','2023-02-15 00:59:39.083367'),
 (16,'admin','0001_initial','2023-02-15 00:59:39.454018'),
 (17,'admin','0002_logentry_remove_auto_add','2023-02-15 00:59:39.581168'),
 (18,'admin','0003_logentry_add_action_flag_choices','2023-02-15 00:59:39.776712'),
 (19,'sessions','0001_initial','2023-02-15 00:59:40.102395'),
 (20,'transport','0001_initial','2023-02-22 18:10:36.899950'),
 (21,'transport','0002_alter_client_prenom','2023-02-22 19:20:03.686346'),
 (22,'transport','0003_alter_reservation_date','2023-02-22 19:35:24.961569'),
 (23,'transport','0004_rename_nombre_de_place_place_nombre_de_place_restant','2023-02-23 19:04:57.116217'),
 (24,'transport','0005_place_disponibilite_and_more','2023-02-23 19:58:01.325453'),
 (25,'transport','0006_reserve_ville','2023-03-10 18:19:36.401795'),
 (26,'transport','0007_remove_client_email_remove_client_telephone','2023-03-13 17:14:01.714592'),
 (27,'transport','0008_client_email_client_telephone','2023-03-13 17:52:09.187212'),
 (28,'transport','0009_client_motdepass_client_nomutisateur','2023-03-29 16:44:16.953949'),
 (29,'transport','0010_courier_reserve_nometprenom','2023-04-06 13:07:31.703756'),
 (30,'transport','0011_rename_nometdeexpediteur_courier_nometprenomdeexpediteur_and_more','2023-04-06 13:13:13.618766'),
 (31,'transport','0012_rename_cnib_courier_cnib_courier_validerarrive_and_more','2023-04-23 01:40:36.229861');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'contenttypes','contenttype'),
 (5,'sessions','session'),
 (6,'account','user'),
 (7,'transport','car'),
 (8,'transport','reservation'),
 (9,'transport','voyages'),
 (10,'transport','client'),
 (11,'transport','place'),
 (12,'transport','voyage_programmer'),
 (13,'transport','reserve'),
 (14,'transport','ville'),
 (15,'transport','courier');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_contenttype','Can add content type'),
 (14,4,'change_contenttype','Can change content type'),
 (15,4,'delete_contenttype','Can delete content type'),
 (16,4,'view_contenttype','Can view content type'),
 (17,5,'add_session','Can add session'),
 (18,5,'change_session','Can change session'),
 (19,5,'delete_session','Can delete session'),
 (20,5,'view_session','Can view session'),
 (21,6,'add_user','Can add user'),
 (22,6,'change_user','Can change user'),
 (23,6,'delete_user','Can delete user'),
 (24,6,'view_user','Can view user'),
 (25,7,'add_car','Can add car'),
 (26,7,'change_car','Can change car'),
 (27,7,'delete_car','Can delete car'),
 (28,7,'view_car','Can view car'),
 (29,8,'add_reservation','Can add reservation'),
 (30,8,'change_reservation','Can change reservation'),
 (31,8,'delete_reservation','Can delete reservation'),
 (32,8,'view_reservation','Can view reservation'),
 (33,9,'add_voyages','Can add voyages'),
 (34,9,'change_voyages','Can change voyages'),
 (35,9,'delete_voyages','Can delete voyages'),
 (36,9,'view_voyages','Can view voyages'),
 (37,10,'add_client','Can add client'),
 (38,10,'change_client','Can change client'),
 (39,10,'delete_client','Can delete client'),
 (40,10,'view_client','Can view client'),
 (41,11,'add_place','Can add place'),
 (42,11,'change_place','Can change place'),
 (43,11,'delete_place','Can delete place'),
 (44,11,'view_place','Can view place'),
 (45,12,'add_voyage_programmer','Can add voyage_programmer'),
 (46,12,'change_voyage_programmer','Can change voyage_programmer'),
 (47,12,'delete_voyage_programmer','Can delete voyage_programmer'),
 (48,12,'view_voyage_programmer','Can view voyage_programmer'),
 (49,13,'add_reserve','Can add reserve'),
 (50,13,'change_reserve','Can change reserve'),
 (51,13,'delete_reserve','Can delete reserve'),
 (52,13,'view_reserve','Can view reserve'),
 (53,14,'add_ville','Can add ville'),
 (54,14,'change_ville','Can change ville'),
 (55,14,'delete_ville','Can delete ville'),
 (56,14,'view_ville','Can view ville'),
 (57,15,'add_courier','Can add courier'),
 (58,15,'change_courier','Can change courier'),
 (59,15,'delete_courier','Can delete courier'),
 (60,15,'view_courier','Can view courier');
INSERT INTO "account_user" ("id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined","profil_photo","role","phone") VALUES (1,'pbkdf2_sha256$390000$bFOdoB98reWvl5YGYvyLln$PXmgEBNzzw+G9T+S7QBAPq/YZBLJ1WYESHoafF17PyE=','2023-04-22 21:08:46.564531',0,'feuble226','FAFFA','ijncdcdc','feublelecfa06@gmail.com',0,1,'2023-02-15 01:40:05.917733','',NULL,'+22678789809'),
 (2,'pbkdf2_sha256$390000$998GQIlXMjw3fckGYJuz6L$jOtksJV6nSNuVgIg9ZN2lgC//q/gOnQARVU1IaCnWEE=','2023-03-16 23:57:52.584265',1,'feuble','','','hjjdhju@gmail.com',1,1,'2023-02-22 18:12:22.947458','',NULL,''),
 (3,'pbkdf2_sha256$390000$M80LbfTtU5fuvBGhfSD2El$ilbyUGkfBJ3uQkSP1L3aWWKUS3pljyQseYYzr5lm1bk=','2023-03-30 19:34:21.721723',0,'user','Faïçal','LENGANE','abdoulfaicallengane@gmail.com',0,1,'2023-03-30 19:34:09.739531','',NULL,'+22673315768'),
 (4,'pbkdf2_sha256$390000$YRTflRe8L9wsA9Inke1Ree$Ffjj2FKobvlntEamdN0FvfHge1vhQxGhBoep7LVvKPY=','2023-04-08 18:17:39.176145',1,'admin','','','admin@gmail.com',1,1,'2023-04-08 18:17:06.485715','',NULL,'');
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (1,'1','Mercedes',1,'[{"added": {}}]',7,2,'2023-02-22 18:13:40.878816'),
 (2,'1','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:28:29.858217'),
 (3,'11','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:52.439289'),
 (4,'10','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:52.520433'),
 (5,'9','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:52.638899'),
 (6,'8','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:52.799591'),
 (7,'7','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:52.958968'),
 (8,'6','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.096251'),
 (9,'5','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.214932'),
 (10,'4','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.348228'),
 (11,'3','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.406305'),
 (12,'2','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.543427'),
 (13,'1','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-22 21:29:53.655836'),
 (14,'30','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.113785'),
 (15,'29','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.181096'),
 (16,'28','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.247441'),
 (17,'27','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.357679'),
 (18,'25','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.435825'),
 (19,'24','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.513139'),
 (20,'23','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.579612'),
 (21,'22','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.646081'),
 (22,'21','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:06:06.720443'),
 (23,'34','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:25:28.312293'),
 (24,'33','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:25:28.369021'),
 (25,'32','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:25:28.438371'),
 (26,'31','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 20:25:28.699756'),
 (27,'34','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 21:00:34.199803'),
 (28,'34','Lengane Abdoul Faycal - ouaga - bobo',3,'',8,2,'2023-02-23 21:14:11.700532'),
 (29,'1','Ouagadougou',1,'[{"added": {}}]',14,2,'2023-03-10 18:20:09.776472'),
 (30,'2','Bobo-Douilasso',1,'[{"added": {}}]',14,2,'2023-03-10 18:20:32.657964'),
 (31,'3','Tenkodogo',1,'[{"added": {}}]',14,2,'2023-03-10 18:20:45.073109'),
 (32,'4','Koudougou',1,'[{"added": {}}]',14,2,'2023-03-10 18:20:56.053756'),
 (33,'6','fay leng',2,'[{"changed": {"fields": ["NomUtisateur"]}}]',10,4,'2023-04-08 20:13:53.082466'),
 (34,'6','fay leng',2,'[{"changed": {"fields": ["NomUtisateur"]}}]',10,4,'2023-04-08 20:14:03.346736'),
 (35,'1','Lengane Abdoul Faycal',2,'[{"changed": {"fields": ["NomUtisateur"]}}]',10,4,'2023-04-08 20:14:28.719896');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('n5as9gc0sqqc9pgwq4xixezs1w5uzg0q','.eJxVjMsOwiAQRf-FtSEMDwGX7vsNZAamUjU0Ke3K-O_apAvd3nPOfYmE21rT1nlJUxEXocXpdyPMD247KHdst1nmua3LRHJX5EG7HObCz-vh_h1U7PVbOzZElqwZo0MCQ4AYiIviPDpnlPdKa_CgIYTgAihkhmwxRwVnbaN4fwDpOzdU:1pVJFb:RAv7iEe2Ief2XTYj7bBd0AkvNlacBab_Jnuj-GQdJtU','2023-03-09 21:35:39.008079'),
 ('gqis881afmmpvfm1v4ixia0xiwzytop1','.eJxVjMsOwiAQRf-FtSHQ4enSvd9AgBmkamhS2pXx35WkC93ec859sRD3rYa90xpmZGcG7PS7pZgf1AbAe2y3heelbeuc-FD4QTu_LkjPy-H-HdTY67dWzlmtJ5fBW_JgHIkklQGpitaOioBUhCe0CtD6CaUiGmp0yZLJlr0_tUw3Qw:1phy2P:MTF0xYPrVHcQwIMfNtU3t6j-9hPgdC358ipFz5ZltUs','2023-04-13 19:34:21.828195'),
 ('0q6wdd8lhcoqt3rx577wqtpvv2b1gw34','.eJxVjEEOwiAQAP_C2RBKgaUevfcNzS67SNW0SWlPxr8bkh70OjOZt5rw2Mt0VNmmmdVVOXX5ZYTpKUsT_MDlvuq0Lvs2k26JPm3V48ryup3t36BgLW3rPZB1AJF7EPBih8wWu2ATxSG4bILHFAmijxKEHaREth8yGu4Msvp8Ac-rN-k:1plD87:Q0Wiue6L7vwUAzV9Xa3Y3TZqXaz9UXoWED4_JbDcyG0','2023-04-22 18:17:39.244673'),
 ('6hpi1c9lpdljhqhc4yshoy5ruelauraq','.eJxVjMsOwiAQRf-FtSGFsQy4dN9vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yQuQonT7xYoPnLdQbpTvTUZW12XOchdkQftcmopP6-H-3dQqJdvzYwQUwp6sMCQjWJkYlDDAIDmDMqQyhYZUCE4stYaxIgu4Gic1qN4fwDdLzbR:1pqKTO:ZVqetj2GydKfI_FWdTai8XAMVecGqRkDwmYPDYvaVM8','2023-05-06 21:08:46.633503');
INSERT INTO "transport_car" ("id","nom","nombre_de_places","capacite_bagage","nombre_de_car") VALUES (1,'Mercedes',100,10000,6);
INSERT INTO "transport_voyages" ("id","ville_depart","ville_arrive","heure_depart","place_number","prix","car_id") VALUES (1,'ouaga','bobo','12:30:00',66,10000,1),
 (4,'Koudougou','Tenkodogo','12:30:00',30,1200,1),
 (5,'Koudougou','Bobo-Douilasso','12:30:00',30,12000,1),
 (6,'Koudougou','Ouagadougou','12:30:00',30,12500,1),
 (7,'Ouagadougou','Tenkodogo','12:30:00',30,12600,1),
 (8,'Ouagadougou','Bobo-Douilasso','12:30:00',38,3000,1),
 (9,'Ouagadougou','Koudougou','12:30:00',30,2000,1),
 (10,'Tenkodogo','Bobo-Douilasso','12:30:00',30,4500,1),
 (11,'Tenkodogo','Koudougou','12:30:00',30,5000,1),
 (12,'Tenkodogo','Ouagadougou','12:30:00',29,2500,1),
 (13,'Bobo-Douilasso','Tenkodogo','12:30:00',35,2000,1),
 (14,'Bobo-Douilasso','Ouagadougou','12:30:00',30,3000,1),
 (15,'Bobo-Douilasso','Koudougou','12:30:00',32,5000,1);
INSERT INTO "transport_place" ("id","date","voyage_id","disponibilite","nombre_de_place_restant") VALUES (1,'2023-12-03',1,1,100),
 (2,'2023-11-03',1,0,-1),
 (3,'2023-04-20',10,0,-1),
 (4,'2023-04-08',10,0,0),
 (5,'2022-11-03',1,0,-2);
INSERT INTO "transport_ville" ("id","nom") VALUES (1,'Ouagadougou'),
 (2,'Bobo-Douilasso'),
 (3,'Tenkodogo'),
 (4,'Koudougou');
INSERT INTO "transport_client" ("id","nom","prenom","addresse","cnib","email","telephone","motDePass","nomUtisateur") VALUES (1,'Lengane','Abdoul Faycal','21Rue',9023194759,'example@example.com','+22661748597','1234','useree'),
 (4,'fay','leng','qw334',1234577,'fay@feuble.com','+22655910476','root','feuble'),
 (5,'adri','saka','qertr',12345,'boingboing@boing.com','+22667980923','root','sakadri'),
 (6,'fay','leng','dfce334',12345,'user@lk.ki','+22667890987','user','user');
INSERT INTO "transport_reserve" ("id","villeDepart","villeArrive","nombreDePlace","typeVoyage","dateReservation","NomEtPrenom") VALUES (1,'Bobo-Douilasso','Koudougou',2,'Aller-Retour','2023-03-31','user'),
 (2,'Bobo-Douilasso','Tenkodogo',2,'Aller-Retour','2023-03-31','user'),
 (3,'Bobo-Douilasso','Tenkodogo',2,'Aller-Retour','2023-03-31','user'),
 (4,'Ouagadougou','Bobo-Douilasso',2,'Aller-Retour','2023-04-20','user'),
 (5,'Ouagadougou','Bobo-Douilasso',2,'Aller-Retour','2023-04-20','user'),
 (6,'Ouagadougou','Bobo-Douilasso',2,'Aller-Retour','2023-04-20','user'),
 (7,'Ouagadougou','Bobo-Douilasso',2,'Aller-Retour','2023-04-20','user'),
 (8,'Ouagadougou','Bobo-Douilasso',2,'Aller-Retour','2023-04-20','user'),
 (9,'Bobo-Douilasso','Tenkodogo',3,'Aller','2023-04-20','user'),
 (10,'Bobo-Douilasso','Tenkodogo',4,'Aller-Retour','2023-04-08','user');
INSERT INTO "transport_reservation" ("id","date","client_id","voyage_id","valider_reservation") VALUES (31,'2022-11-03',1,1,1),
 (32,'2023-11-03',1,1,0),
 (33,'2023-11-03',1,1,0),
 (35,'2023-04-20',6,10,1),
 (36,'2023-04-08',6,10,0);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "account_user_groups_user_id_group_id_4d09af3e_uniq" ON "account_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "account_user_groups_user_id_14345e7b" ON "account_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "account_user_groups_group_id_6c71f749" ON "account_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "account_user_user_permissions_user_id_permission_id_48bdd28b_uniq" ON "account_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "account_user_user_permissions_user_id_cc42d270" ON "account_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "account_user_user_permissions_permission_id_66c44191" ON "account_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "transport_voyages_car_id_53ff8f17" ON "transport_voyages" (
	"car_id"
);
CREATE INDEX IF NOT EXISTS "transport_voyage_programmer_car_id_f863ee94" ON "transport_voyage_programmer" (
	"car_id"
);
CREATE INDEX IF NOT EXISTS "transport_place_voyage_id_a9bc5cc4" ON "transport_place" (
	"voyage_id"
);
CREATE INDEX IF NOT EXISTS "transport_reservation_client_id_58bc8d6f" ON "transport_reservation" (
	"client_id"
);
CREATE INDEX IF NOT EXISTS "transport_reservation_voyage_id_a21299cb" ON "transport_reservation" (
	"voyage_id"
);
COMMIT;
