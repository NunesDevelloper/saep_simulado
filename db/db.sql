- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `saep_db` ;
USE `saep_db` ;

-- -----------------------------------------------------
-- Table `saep_db`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `saep_db`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(120) NOT NULL,
  `senha` VARCHAR(225) NOT NULL,
  `nome` VARCHAR(120) NOT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE INDEX `login_UNIQUE` (`email` ASC) VISIBLE)
;;


-- -----------------------------------------------------
-- Table `saep_db`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `saep_db`.`produto` (
  `idproduto` INT NOT NULL AUTO_INCREMENT,
  `preco` DECIMAL(10,2) NOT NULL,
  `nome` VARCHAR(120) NOT NULL,
  `aplciacao` ENUM("fundação", "acabamento", "estrutura") NOT NULL,
  `unidade_medida` ENUM("kg", "m2", "litros", "uni") NOT NULL DEFAULT 'uni',
  `obs` TEXT NULL,
  PRIMARY KEY (`idproduto`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
;;


-- -----------------------------------------------------
-- Table `saep_db`.`estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `saep_db`.`estoque` (
  `idestoque` INT NOT NULL AUTO_INCREMENT,
  `qtn_minima` INT NOT NULL,
  `qtn` INT NOT NULL,
  `produto_idproduto` INT NOT NULL,
  PRIMARY KEY (`idestoque`, `produto_idproduto`),
  INDEX `fk_estoque_produto_idx` (`produto_idproduto` ASC) VISIBLE,
  CONSTRAINT `fk_estoque_produto`
    FOREIGN KEY (`produto_idproduto`)
    REFERENCES `saep_db`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `saep_db`.`logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `saep_db`.`logs` (
  `idlogs` INT NOT NULL AUTO_INCREMENT,
  `dt_acao` DATETIME NOT NULL DEFAULT now(),
  `is_retirada` TINYINT NOT NULL DEFAULT 0,
  `qtn_acao` INT NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  `estoque_idestoque` INT NOT NULL,
  PRIMARY KEY (`idlogs`, `usuario_idusuario`, `estoque_idestoque`),
  INDEX `fk_logs_usuario1_idx` (`usuario_idusuario` ASC) VISIBLE,
  INDEX `fk_logs_estoque1_idx` (`estoque_idestoque` ASC) VISIBLE,
  CONSTRAINT `fk_logs_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `saep_db`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_logs_estoque1`
    FOREIGN KEY (`estoque_idestoque`)
    REFERENCES `saep_db`.`estoque` (`idestoque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);



