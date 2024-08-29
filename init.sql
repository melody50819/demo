CREATE TABLE `product`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `category` VARCHAR(45) NOT NULL,
  `size` TEXT NULL,
  `unit_price` INT NULL,
  `inventory` INT NULL,
  `color` TEXT NULL,
  PRIMARY KEY (`code`));
