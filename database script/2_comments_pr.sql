CREATE TABLE `comentarios_pr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(70) DEFAULT NULL,
  `projeto` varchar(70) DEFAULT NULL,
  `owner` varchar(70) DEFAULT NULL,
  `body` varchar(4000) DEFAULT NULL,
  `dt_comentario` datetime DEFAULT NULL,
  `number_pr` varchar(15) DEFAULT NULL,
  `author_association` varchar(50) DEFAULT NULL,
  `id_pr` int(11) DEFAULT NULL,
  KEY `idx_comentarios_pr_number_pr` (`number_pr`),
  KEY `idx_comentarios_pr_owner` (`owner`),
  KEY `idx_comentarios_pr_projeto` (`projeto`),
  KEY `idx_comentarios_pr_usuario` (`usuario`),
  KEY `idx_comentarios_pr_id` (`id`),
  KEY `idx_comentarios_pr_body` (`body`(255)),
  KEY `idx_comentarios_pr_id_pr` (`id_pr`)
) ENGINE=MyISAM AUTO_INCREMENT=671300 DEFAULT CHARSET=utf8 COMMENT='			';
