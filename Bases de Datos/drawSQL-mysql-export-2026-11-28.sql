CREATE TABLE `Products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(255) NOT NULL,
    `stock_available` INT NOT NULL DEFAULT 0
);
ALTER TABLE
    `Products` ADD INDEX `products_code_index`(`code`);
CREATE TABLE `Invoices`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` VARCHAR(255) NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` VARCHAR(255) NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
ALTER TABLE
    `Invoices` ADD INDEX `invoices_invoice_number_index`(`invoice_number`);
CREATE TABLE `Products Per Invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `quantity` INT UNSIGNED NOT NULL DEFAULT 1,
    `total_amount` DECIMAL(10, 2) NOT NULL,
    `invoice_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL
);
ALTER TABLE
    `Products Per Invoice` ADD INDEX `products per invoice_invoice_id_index`(`invoice_id`);
ALTER TABLE
    `Products Per Invoice` ADD INDEX `products per invoice_product_id_index`(`product_id`);
CREATE TABLE `Shopping Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Shopping Cart` ADD INDEX `shopping cart_buyer_email_index`(`buyer_email`);
CREATE TABLE `Products Per Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT UNSIGNED NOT NULL DEFAULT 1
);
ALTER TABLE
    `Products Per Cart` ADD INDEX `products per cart_cart_id_index`(`cart_id`);
ALTER TABLE
    `Products Per Cart` ADD INDEX `products per cart_product_id_index`(`product_id`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Products Per Cart` ADD CONSTRAINT `products per cart_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `Shopping Cart`(`id`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `Invoices`(`id`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `Products`(`id`);