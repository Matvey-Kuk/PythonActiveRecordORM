DROP DATABASE IF EXISTS `PyAR`;
CREATE DATABASE `PyAR`;

CREATE TABLE `PyAR`.`TableA`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`TableB_id` int(11) NOT NULL,
	primary key (`id`)
);

CREATE TABLE `PyAR`.`TableB`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`TableA_id` int(11) NOT NULL,
	primary key (`id`)
);