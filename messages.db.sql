BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS `messages` (
	`id`	INTEGER NOT NULL,
	`from_id`	INTEGER,
	`message`	TEXT(280),
	`to_id`	INTEGER,
	`deleted_flag`	BOOLEAN,
	FOREIGN KEY(`from_id`) REFERENCES `family`(`id`),
	FOREIGN KEY(`to_id`) REFERENCES `family`(`id`),
	PRIMARY KEY(`id`)
);
INSERT INTO `messages` VALUES (1,1,'hey just off to the library',2,0);
INSERT INTO `messages` VALUES (2,1,'Want me to bring home pie?',2,0);
INSERT INTO `messages` VALUES (3,2,'Need more apple pie',1,0);
INSERT INTO `messages` VALUES (4,5,'Going to salt a ghost',1,0);
INSERT INTO `messages` VALUES (5,1,'werewoves and vamps',2,0);
INSERT INTO `messages` VALUES (6,5,'need more salt',1,1);
INSERT INTO `messages` VALUES (7,6,'they are comming',3,0);

CREATE TABLE IF NOT EXISTS `family` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`name`	VARCHAR(120),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`),
	PRIMARY KEY(`id`)
);
INSERT INTO `family` VALUES (1,1,'Sam');
INSERT INTO `family` VALUES (2,1,'Dean');
INSERT INTO `family` VALUES (3,2,'Lucy');
INSERT INTO `family` VALUES (4,2,'Jack');
INSERT INTO `family` VALUES (5,1,'Bobby');
INSERT INTO `family` VALUES (6,2,'Helen');
INSERT INTO `family` VALUES (7,1,'Terry');

CREATE TABLE IF NOT EXISTS `user` (
	`id`	INTEGER NOT NULL,
	`alexa_id`	VARCHAR(230) NOT NULL UNIQUE,
	PRIMARY KEY(`id`)
);
INSERT INTO `user` VALUES (1,'999');
INSERT INTO `user` VALUES (2,'666');
COMMIT;
