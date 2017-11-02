-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: register
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userdata` (
  `usernumber` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `salt` varchar(64) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`usernumber`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES (29,'bob1111','changyaoxu1995@gmail.com',NULL,'55587a910882016321201e6ebbc9f595'),(30,'jackzhang','changyaoxu1995@gmail.com',NULL,'23b4b8acbec3f12180eb034a2d5203ab'),(31,'bobxu','changyaoxu1994@gmail.com',NULL,'e10adc3949ba59abbe56e057f20f883e'),(32,'bobxu','changyaoxu1994@gmail.com',NULL,'cc831afa7736e73484746816cc600029'),(33,'leo1','changyaoxu1995@hotmail.com',NULL,'b29e09481d71303ace51676fc925e08b'),(34,'leo2','xu@gamil.com',NULL,'9fab6755cd2e8817d3e73b0978ca54a6'),(35,'leo2','xu@gamil.com',NULL,'789456123'),(36,'leo2','xu@gamil.com',NULL,'789456123'),(37,'leo3','c@gmail.com',NULL,'bd7008048be60c06a53fd13d673b8416'),(38,'leo4','c@gmai.com',NULL,'43f18c173d928930b36878cd26802582'),(39,'12344','123@163.com',NULL,'8795a3cd2ca1f7f1530b3bb4e8baf650'),(40,'nancy','123@gmail.com',NULL,'d0970714757783e6cf17b26fb8e2298f'),(41,'n123456789','c@gmai.com',NULL,'809f09f73d5a61070477b1d676155e25'),(42,'n123456789','c@gmai.com',NULL,'25f9e794323b453885f5181f1b624d0b'),(43,'test','test@g.com',NULL,'362462b6e94b3a1778e71298fffdcbab');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-29 15:46:57
