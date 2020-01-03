CREATE TABLE `pr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(50) NOT NULL,
  `type_user` varchar(40) DEFAULT NULL,
  `site_admin` varchar(20) DEFAULT NULL,
  `nome_projeto` varchar(80) DEFAULT NULL,
  `owner` varchar(70) DEFAULT NULL,
  `id_git` int(15) DEFAULT NULL,
  `number_pr` varchar(15) DEFAULT NULL,
  `title` varchar(350) DEFAULT NULL,
  `merge` char(9) DEFAULT NULL,
  `dt_criado` datetime DEFAULT NULL,
  `dt_fechado` datetime DEFAULT NULL,
  `linguagem` varchar(60) DEFAULT NULL,
  `comments_qtde` int(11) DEFAULT NULL,
  `review_comments` int(11) DEFAULT NULL,
  `commits` int(11) DEFAULT NULL,
  `additions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL,
  `changed_files` int(11) DEFAULT NULL,
  `author_association` varchar(50) DEFAULT NULL,
  `qtde_merge` int(11) DEFAULT NULL,
  `qtde_comentario` int(3) DEFAULT NULL,
  `qtde_commit` int(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`),
  KEY `nome_projeto` (`nome_projeto`),
  KEY `i_linguagem` (`linguagem`),
  KEY `idx_pr_number_pr` (`number_pr`),
  KEY `idx_pr_user` (`user`),
  KEY `idx_pr_nome_projeto` (`nome_projeto`),
  FULLTEXT KEY `idx_pr_owner` (`owner`)
) ENGINE=MyISAM AUTO_INCREMENT=1111561948 DEFAULT CHARSET=utf8;
