CREATE TABLE `commits_pr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(60) DEFAULT NULL,
  `dt_commit` datetime DEFAULT NULL,
  `projeto` varchar(60) DEFAULT NULL,
  `owner` varchar(60) DEFAULT NULL,
  `sha` varchar(60) DEFAULT NULL,
  `commiter` varchar(60) DEFAULT NULL,
  `data_aceito` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_commit_todos_projeto` (`projeto`),
  KEY `idx_commit_todos_sha` (`sha`),
  KEY `idx_commit_todos_usuario` (`usuario`),
  KEY `idx_commit_todos_owner` (`owner`),
  KEY `idx_commits_pr_id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1865959 DEFAULT CHARSET=utf8;
