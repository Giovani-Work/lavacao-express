-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LavacaoEspress
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `LavacaoEspress` ;

-- -----------------------------------------------------
-- Schema LavacaoEspress
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LavacaoEspress` DEFAULT CHARACTER SET utf8mb4 ;
SHOW WARNINGS;
USE `LavacaoEspress` ;

-- -----------------------------------------------------
-- Table `LavacaoEspress`.`profile`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `LavacaoEspress`.`profile` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `LavacaoEspress`.`profile` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `email` VARCHAR(320) NOT NULL,
  `cell_phone` VARCHAR(15) NULL,
  `photo` VARCHAR(50) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `LavacaoEspress`.`address`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `LavacaoEspress`.`address` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `LavacaoEspress`.`address` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `street` VARCHAR(200) NOT NULL,
  `number` VARCHAR(25) NOT NULL,
  `district` VARCHAR(100) NULL,
  `city` VARCHAR(100) NULL,
  `state` VARCHAR(100) NULL,
  `postal_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `LavacaoEspress`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `LavacaoEspress`.`user` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `LavacaoEspress`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(100) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `profile_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `is_client` TINYINT NOT NULL,
  `is_manager` TINYINT NOT NULL,
  `is_worker` TINYINT NOT NULL,
  PRIMARY KEY (`id`, `profile_id`, `address_id`),
  CONSTRAINT `fk_user_profile`
    FOREIGN KEY (`profile_id`)
    REFERENCES `LavacaoEspress`.`profile` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_address1`
    FOREIGN KEY (`address_id`)
    REFERENCES `LavacaoEspress`.`address` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `login_UNIQUE` ON `LavacaoEspress`.`user` (`login` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_user_profile_idx` ON `LavacaoEspress`.`user` (`profile_id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_user_address1_idx` ON `LavacaoEspress`.`user` (`address_id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `LavacaoEspress`.`permission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `LavacaoEspress`.`permission` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `LavacaoEspress`.`permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  `is_active` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `LavacaoEspress`.`user_permissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `LavacaoEspress`.`user_permissions` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `LavacaoEspress`.`user_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permissions_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`, `permissions_id`),
  CONSTRAINT `fk_user_permissions_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `LavacaoEspress`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_permissions_permissions1`
    FOREIGN KEY (`permissions_id`)
    REFERENCES `LavacaoEspress`.`permission` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_user_permissions_user1_idx` ON `LavacaoEspress`.`user_permissions` (`user_id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_user_permissions_permissions1_idx` ON `LavacaoEspress`.`user_permissions` (`permissions_id` ASC) VISIBLE;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
