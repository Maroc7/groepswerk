BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "t_user" (
	"pk_id"	INTEGER NOT NULL,
	"f_firstname"	TEXT NOT NULL,
	"f_lastname"	TEXT NOT NULL,
	"f_mail"	TEXT NOT NULL UNIQUE,
	"f_website"	TEXT,
	PRIMARY KEY("pk_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "t_project" (
	"pk_id"	INTEGER NOT NULL,
	"f_name"	TEXT NOT NULL,
	"f_description"	TEXT,
	"f_start_date"	TEXT,
	"f_end_date"	TEXT,
	"fk_client_id"	INTEGER,
	PRIMARY KEY("pk_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "t_client" (
	"pk_id"	INTEGER NOT NULL,
	"f_firstname"	TEXT NOT NULL,
	"f_lastname"	TEXT NOT NULL,
	"f_mail"	TEXT NOT NULL UNIQUE,
	"f_website"	TEXT,
	"fk_project"	INTEGER,
	PRIMARY KEY("pk_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "t_task" (
	"pk_id"	INTEGER NOT NULL,
	"f_name"	TEXT NOT NULL,
	"f_start_date"	INTEGER,
	"f_end_date"	INTEGER,
	"f_status"	TEXT,
	"fk_user_id"	INTEGER,
	"fk_project_id"	INTEGER,
	PRIMARY KEY("pk_id" AUTOINCREMENT),
	FOREIGN KEY("fk_user_id") REFERENCES "t_user"("pk_id")
);
INSERT INTO "t_user" ("pk_id","f_firstname","f_lastname","f_mail","f_website") VALUES (1,'Bart','Denayer','bartmail@mail.com','www.bart.be'),
 (2,'Hamza','Maroc','hamza@mail.com','www.hamza.be'),
 (3,'Akhmed','Barshigov','akhmed@mail.com','www.akhmed.be'),
 (4,'Ilyas','Caluwe','ilyas.caluwe@gmail.com','www.ilyas.be'),
 (10,'kamal','maroc','kamalmaroc@gmail.con','www.kamal');
INSERT INTO "t_project" ("pk_id","f_name","f_description","f_start_date","f_end_date","fk_client_id") VALUES (1,'pm software','a programe to do project management tasks, this is the assignment for a group project at Syntra','15/10/2022','15/01/2023',1);
INSERT INTO "t_client" ("pk_id","f_firstname","f_lastname","f_mail","f_website","fk_project") VALUES (1,'clientfirstname','clientlastname','client_mail@clientcompany.com','www.client1.com',1);
INSERT INTO "t_task" ("pk_id","f_name","f_start_date","f_end_date","f_status","fk_user_id","fk_project_id") VALUES (4,'database','10/11/2022','10/12/2022','Finished by Ilyas Caluwe',4,1),
 (5,'menu','9/11/2022','11/11/2022','Finished by Hamza',2,1),
 (6,'client module','10/11/2022','19/12/2022','Finished by Akhmed',3,1),
 (7,'project module','10/10/2022','10/11/2022','Finished by Bart',1,1),
 (8,'newtask','10/10/2022','10/12/2022','ongoing',NULL,NULL);
COMMIT;
