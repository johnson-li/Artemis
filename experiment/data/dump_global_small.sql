-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: serviceid_db
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1-log

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
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deployment`
--

DROP TABLE IF EXISTS `deployment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deployment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datacenter` varchar(32) DEFAULT NULL,
  `domain` varchar(32) DEFAULT NULL,
  `loadbalancer` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`,`datacenter`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deployment`
--

LOCK TABLES `deployment` WRITE;
/*!40000 ALTER TABLE `deployment` DISABLE KEYS */;
INSERT INTO `deployment` VALUES (1,'usus-eat1','serviceid.xuebing.li','usus-eat1'),(2,'usus-eat4','serviceid.xuebing.li','usus-eat4'),(3,'usus-cel1','serviceid.xuebing.li','usus-cel1'),(4,'usus-wet1','serviceid.xuebing.li','usus-wet1'),(5,'usus-wet2','serviceid.xuebing.li','usus-wet2'),(6,'usus-wet3','serviceid.xuebing.li','usus-wet3'),(7,'eupe-wet1','serviceid.xuebing.li','eupe-wet1'),(8,'eupe-wet2','serviceid.xuebing.li','eupe-wet2'),(9,'eupe-wet3','serviceid.xuebing.li','eupe-wet3'),(10,'eupe-wet4','serviceid.xuebing.li','eupe-wet4'),(11,'eupe-wet6','serviceid.xuebing.li','eupe-wet6'),(12,'eupe-noh1','serviceid.xuebing.li','eupe-noh1'),(13,'asia-eat1','serviceid.xuebing.li','asia-eat1'),(14,'asia-eat2','serviceid.xuebing.li','asia-eat2'),(15,'asia-sot1','serviceid.xuebing.li','asia-sot1'),(16,'asia-not1','serviceid.xuebing.li','asia-not1'),(17,'asia-not2','serviceid.xuebing.li','asia-not2'),(18,'asia-not3','serviceid.xuebing.li','asia-not3'),(19,'asia-soh1','serviceid.xuebing.li','asia-soh1'),(20,'auia-sot1','serviceid.xuebing.li','auia-sot1'),(21,'soca-eat1','serviceid.xuebing.li','soca-eat1'),(22,'noca-not1','serviceid.xuebing.li','noca-not1');
/*!40000 ALTER TABLE `deployment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intra`
--

DROP TABLE IF EXISTS `intra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(32) DEFAULT NULL,
  `server` varchar(32) DEFAULT NULL,
  `datacenter` varchar(32) DEFAULT NULL,
  `sid` varchar(32) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intra`
--

LOCK TABLES `intra` WRITE;
/*!40000 ALTER TABLE `intra` DISABLE KEYS */;
INSERT INTO `intra` VALUES (1,'serviceid.xuebing.li','server','usus-eat1','11.11.11.11',1),(2,'serviceid.xuebing.li','server','usus-eat4','11.11.11.11',1),(3,'serviceid.xuebing.li','server','usus-cel1','11.11.11.11',1),(4,'serviceid.xuebing.li','server','usus-wet1','11.11.11.11',1),(5,'serviceid.xuebing.li','server','usus-wet2','11.11.11.11',1),(6,'serviceid.xuebing.li','server','usus-wet3','11.11.11.11',1),(7,'serviceid.xuebing.li','server','eupe-wet1','11.11.11.11',1),(8,'serviceid.xuebing.li','server','eupe-wet2','11.11.11.11',1),(9,'serviceid.xuebing.li','server','eupe-wet3','11.11.11.11',1),(10,'serviceid.xuebing.li','server','eupe-wet4','11.11.11.11',1),(11,'serviceid.xuebing.li','server','eupe-wet6','11.11.11.11',1),(12,'serviceid.xuebing.li','server','eupe-noh1','11.11.11.11',1),(13,'serviceid.xuebing.li','server','asia-eat1','11.11.11.11',1),(14,'serviceid.xuebing.li','server','asia-eat2','11.11.11.11',1),(15,'serviceid.xuebing.li','server','asia-sot1','11.11.11.11',1),(16,'serviceid.xuebing.li','server','asia-not1','11.11.11.11',1),(17,'serviceid.xuebing.li','server','asia-not2','11.11.11.11',1),(18,'serviceid.xuebing.li','server','asia-not3','11.11.11.11',1),(19,'serviceid.xuebing.li','server','asia-soh1','11.11.11.11',1),(20,'serviceid.xuebing.li','server','auia-sot1','11.11.11.11',1),(21,'serviceid.xuebing.li','server','soca-eat1','11.11.11.11',1),(22,'serviceid.xuebing.li','server','noca-not1','11.11.11.11',1);
/*!40000 ALTER TABLE `intra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `measurements`
--

DROP TABLE IF EXISTS `measurements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `measurements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dc` varchar(32) DEFAULT NULL,
  `client` varchar(32) DEFAULT NULL,
  `latency` float DEFAULT NULL,
  `ts` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurements`
--

LOCK TABLES `measurements` WRITE;
/*!40000 ALTER TABLE `measurements` DISABLE KEYS */;
INSERT INTO `measurements` VALUES (1,'noca-not1','13.53.136.176',106.47,1601200268260),(2,'soca-eat1','13.53.136.176',232.495,1601200268260),(3,'eupe-noh1','13.53.136.176',13.513,1601200268260),(4,'asia-eat1','13.53.136.176',277.84,1601200268260),(5,'auia-sot1','13.53.136.176',305.08,1601200268260),(6,'usus-cel1','13.53.136.176',124.591,1601200268260),(7,'noca-not1','3.12.165.205',25.317,1601200285061),(8,'soca-eat1','3.12.165.205',141.76,1601200285061),(9,'eupe-noh1','3.12.165.205',125.754,1601200285061),(10,'asia-eat1','3.12.165.205',179.101,1601200285061),(11,'auia-sot1','3.12.165.205',206.098,1601200285061),(12,'usus-cel1','3.12.165.205',27.247,1601200285061),(13,'noca-not1','34.239.151.143',15.768,1601200299220),(14,'soca-eat1','34.239.151.143',130.51,1601200299220),(15,'eupe-noh1','34.239.151.143',114.826,1601200299220),(16,'asia-eat1','34.239.151.143',183.088,1601200299220),(17,'auia-sot1','34.239.151.143',203.17,1601200299220),(18,'usus-cel1','34.239.151.143',29.174,1601200299220),(19,'noca-not1','54.183.177.242',81.785,1601200343200),(20,'soca-eat1','54.183.177.242',168.275,1601200343200),(21,'eupe-noh1','54.183.177.242',185.368,1601200343200),(22,'asia-eat1','54.183.177.242',141.831,1601200343200),(23,'auia-sot1','54.183.177.242',146.717,1601200343200),(24,'usus-cel1','54.183.177.242',55.971,1601200343200),(25,'auia-sot1','18.237.23.235',169.268,1601200555880),(26,'soca-eat1','18.237.23.235',182.219,1601200555880),(27,'usus-cel1','18.237.23.235',62.634,1601200555880),(28,'eupe-noh1','18.237.23.235',190.691,1601200555880),(29,'asia-eat1','18.237.23.235',132.231,1601200555880),(30,'noca-not1','18.237.23.235',86.891,1601200555880),(31,'auia-sot1','15.165.70.216',158.546,1601200657910),(32,'soca-eat1','15.165.70.216',294.218,1601200657910),(33,'usus-cel1','15.165.70.216',152.803,1601200657910),(34,'eupe-noh1','15.165.70.216',284.258,1601200657910),(35,'auia-sot1','18.183.238.70',144.246,1601200684087),(36,'asia-eat1','15.165.70.216',67.602,1601200657910),(37,'soca-eat1','18.183.238.70',253.004,1601200684087),(38,'noca-not1','15.165.70.216',184.966,1601200657910),(39,'usus-cel1','18.183.238.70',125.684,1601200684087),(40,'eupe-noh1','18.183.238.70',258.114,1601200684087),(41,'asia-eat1','18.183.238.70',38.499,1601200684087),(42,'noca-not1','18.183.238.70',152.333,1601200684087),(43,'auia-sot1','13.235.57.112',150.763,1601200619913),(44,'soca-eat1','13.235.57.112',348.875,1601200619913),(45,'usus-cel1','13.235.57.112',233.591,1601200619913),(46,'eupe-noh1','13.235.57.112',262.985,1601200619913),(47,'asia-eat1','13.235.57.112',108.958,1601200619913),(48,'noca-not1','13.235.57.112',238.574,1601200619913),(49,'noca-not1','13.239.112.40',213.622,1601200931308),(50,'eupe-noh1','13.239.112.40',316.828,1601200931308),(51,'asia-eat1','13.239.112.40',147.276,1601200931308),(52,'usus-cel1','13.239.112.40',185.781,1601200931308),(53,'soca-eat1','13.239.112.40',295.362,1601200931308),(54,'auia-sot1','13.239.112.40',2.241,1601200931308),(55,'noca-not1','54.179.194.255',216.482,1601200981871),(56,'eupe-noh1','54.179.194.255',319.372,1601200981871),(57,'asia-eat1','54.179.194.255',49.338,1601200981871),(58,'usus-cel1','54.179.194.255',186.159,1601200981871),(59,'soca-eat1','54.179.194.255',321.532,1601200981871),(60,'auia-sot1','54.179.194.255',93.531,1601200981871),(61,'noca-not1','18.177.136.175',156.926,1601201012802),(62,'eupe-noh1','18.177.136.175',256.313,1601201012802),(63,'asia-eat1','18.177.136.175',41.291,1601201012802),(64,'usus-cel1','18.177.136.175',126.469,1601201012802),(65,'soca-eat1','18.177.136.175',251.503,1601201012802),(66,'noca-not1','15.222.63.70',1.442,1601201029926),(67,'eupe-noh1','15.222.63.70',122.624,1601201029926),(68,'auia-sot1','18.177.136.175',143.264,1601201012802),(69,'asia-eat1','15.222.63.70',178.964,1601201029926),(70,'usus-cel1','15.222.63.70',29.071,1601201029926),(71,'soca-eat1','15.222.63.70',143.511,1601201029926),(72,'auia-sot1','15.222.63.70',213.88,1601201029926),(73,'usus-cel1','35.158.103.110',107.95,1601201205767),(74,'soca-eat1','35.158.103.110',215.456,1601201205767),(75,'noca-not1','35.158.103.110',90.579,1601201205767),(76,'eupe-noh1','35.158.103.110',29.286,1601201205767),(77,'asia-eat1','35.158.103.110',258.948,1601201205767),(78,'auia-sot1','35.158.103.110',289.157,1601201205767),(79,'usus-cel1','52.50.155.255',103.616,1601201214692),(80,'soca-eat1','52.50.155.255',211.995,1601201214692),(81,'noca-not1','52.50.155.255',87.904,1601201214692),(82,'eupe-noh1','52.50.155.255',44.694,1601201214692),(83,'asia-eat1','52.50.155.255',258.415,1601201214692),(84,'auia-sot1','52.50.155.255',283.999,1601201214692),(85,'usus-cel1','35.180.116.229',103.022,1601201236625),(86,'soca-eat1','35.180.116.229',207.555,1601201236625),(87,'noca-not1','35.180.116.229',83.807,1601201236625),(88,'eupe-noh1','35.180.116.229',35.812,1601201236625),(89,'asia-eat1','35.180.116.229',258.536,1601201236625),(90,'auia-sot1','35.180.116.229',280.43,1601201236625),(91,'usus-cel1','35.178.190.171',96.657,1601201227777),(92,'soca-eat1','35.178.190.171',202.103,1601201227777),(93,'noca-not1','35.178.190.171',76.707,1601201227777),(94,'eupe-noh1','35.178.190.171',36.334,1601201227777),(95,'asia-eat1','35.178.190.171',251.262,1601201227777),(96,'auia-sot1','35.178.190.171',275.606,1601201227777);
/*!40000 ALTER TABLE `measurements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transfer_time`
--

DROP TABLE IF EXISTS `transfer_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transfer_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_ip` varchar(32) DEFAULT NULL,
  `router_ip` varchar(32) DEFAULT NULL,
  `server_ip` varchar(32) DEFAULT NULL,
  `hostname` varchar(1024) DEFAULT NULL,
  `client_region` varchar(1024) DEFAULT NULL,
  `router_region` varchar(1024) DEFAULT NULL,
  `server_region` varchar(1024) DEFAULT NULL,
  `service_id_transfer_time` int(11) DEFAULT NULL,
  `service_id_handshake_time` int(11) DEFAULT NULL,
  `dns_query_time` int(11) DEFAULT NULL,
  `dns_transfer_time` int(11) DEFAULT NULL,
  `dns_handshake_time` int(11) DEFAULT NULL,
  `anycast_transfer_time` int(11) DEFAULT NULL,
  `anycast_handshake_time` int(11) DEFAULT NULL,
  `service_plt_time` int(11) DEFAULT NULL,
  `dns_plt_time` int(11) DEFAULT NULL,
  `anycast_plt_time` int(11) DEFAULT NULL,
  `bind_server_ip` varchar(32) DEFAULT NULL,
  `website` varchar(32) DEFAULT NULL,
  `timestamp` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfer_time`
--

LOCK TABLES `transfer_time` WRITE;
/*!40000 ALTER TABLE `transfer_time` DISABLE KEYS */;
INSERT INTO `transfer_time` VALUES (1,'13.53.136.176','35.228.26.105','35.228.62.197','ip-172-31-7-128','eu-north-1','hestia-europe-north1-c-server','usus-cel1',32527,19287,52,27495,14795,27615,14827,-1,-1,-1,'35.228.62.197','-1',1601200268260),(2,'13.53.136.176','35.228.26.105','35.228.62.197','ip-172-31-7-128','eu-north-1','hestia-europe-north1-c-server','usus-cel1',29537,17563,0,27699,14829,27643,14814,-1,-1,-1,'35.228.62.197','-1',1601200268260),(3,'13.53.136.176','35.228.26.105','35.228.62.197','ip-172-31-7-128','eu-north-1','hestia-europe-north1-c-server','usus-cel1',29224,16324,0,27843,14915,27764,14932,-1,-1,-1,'35.228.62.197','-1',1601200268260),(4,'3.12.165.205','34.95.45.42','35.203.28.222','ip-172-31-13-101','us-east-2','hestia-northamerica-northeast1-c-server','usus-cel1',61846,33992,30,55345,28214,56357,28192,-1,-1,-1,'35.203.28.222','-1',1601200285061),(5,'13.53.136.176','35.228.26.105','35.228.62.197','ip-172-31-7-128','eu-north-1','hestia-europe-north1-c-server','usus-cel1',28453,16457,0,27824,14874,25589,14667,-1,-1,-1,'35.228.62.197','-1',1601200268260),(6,'3.12.165.205','34.95.45.42','35.203.28.222','ip-172-31-13-101','us-east-2','hestia-northamerica-northeast1-c-server','usus-cel1',57303,29605,0,57758,30661,55418,28167,-1,-1,-1,'35.203.28.222','-1',1601200285061),(7,'34.239.151.143','34.121.219.89','35.203.28.222','ip-172-31-73-70','us-east-1','hestia-us-central1-c-server','usus-cel1',61965,44568,115,38402,20910,66540,35266,-1,-1,-1,'35.203.28.222','-1',1601200299220),(8,'13.53.136.176','35.228.26.105','35.228.62.197','ip-172-31-7-128','eu-north-1','hestia-europe-north1-c-server','usus-cel1',30515,18603,0,28004,14725,27773,14869,-1,-1,-1,'35.228.62.197','-1',1601200268260),(9,'3.12.165.205','34.95.45.42','35.203.28.222','ip-172-31-13-101','us-east-2','hestia-northamerica-northeast1-c-server','usus-cel1',56747,29525,0,57699,30462,59117,28525,-1,-1,-1,'35.203.28.222','-1',1601200285061),(10,'34.239.151.143','34.121.219.89','35.203.28.222','ip-172-31-73-70','us-east-1','hestia-us-central1-c-server','usus-cel1',58544,41581,0,38064,20393,63839,32669,-1,-1,-1,'35.203.28.222','-1',1601200299220),(11,'3.12.165.205','34.95.45.42','35.203.28.222','ip-172-31-13-101','us-east-2','hestia-northamerica-northeast1-c-server','usus-cel1',56423,29884,0,55543,28320,57486,28383,-1,-1,-1,'35.203.28.222','-1',1601200285061),(12,'34.239.151.143','34.121.219.89','35.203.28.222','ip-172-31-73-70','us-east-1','hestia-us-central1-c-server','usus-cel1',58331,41540,0,37693,21057,63823,32625,-1,-1,-1,'35.203.28.222','-1',1601200299220),(13,'3.12.165.205','34.95.45.42','35.203.28.222','ip-172-31-13-101','us-east-2','hestia-northamerica-northeast1-c-server','usus-cel1',57358,29270,0,56675,29564,55319,27938,-1,-1,-1,'35.203.28.222','-1',1601200285061),(14,'34.239.151.143','34.121.219.89','35.203.28.222','ip-172-31-73-70','us-east-1','hestia-us-central1-c-server','usus-cel1',58590,41628,0,37063,19375,63822,32603,-1,-1,-1,'35.203.28.222','-1',1601200299220),(15,'34.239.151.143','34.121.219.89','35.203.28.222','ip-172-31-73-70','us-east-1','hestia-us-central1-c-server','usus-cel1',57779,40068,0,37180,19444,64162,32955,-1,-1,-1,'35.203.28.222','-1',1601200299220),(16,'54.183.177.242','35.228.26.105','34.123.139.117','ip-172-31-5-90','us-west-1','hestia-europe-north1-c-server','usus-cel1',257256,198011,4,119848,60763,376318,188849,-1,-1,-1,'34.123.139.117','-1',1601200343200),(17,'54.183.177.242','35.228.26.105','34.123.139.117','ip-172-31-5-90','us-west-1','hestia-europe-north1-c-server','usus-cel1',253981,195014,0,120328,61104,374599,188648,-1,-1,-1,'34.123.139.117','-1',1601200343200),(18,'54.183.177.242','35.228.26.105','34.123.139.117','ip-172-31-5-90','us-west-1','hestia-europe-north1-c-server','usus-cel1',254428,195155,0,118958,59997,376915,189331,-1,-1,-1,'34.123.139.117','-1',1601200343200),(19,'54.183.177.242','35.228.26.105','34.123.139.117','ip-172-31-5-90','us-west-1','hestia-europe-north1-c-server','usus-cel1',254441,195569,0,119316,59994,376545,189057,-1,-1,-1,'34.123.139.117','-1',1601200343200),(20,'54.183.177.242','35.228.26.105','34.123.139.117','ip-172-31-5-90','us-west-1','hestia-europe-north1-c-server','usus-cel1',254649,196038,0,119348,60457,376454,188740,-1,-1,-1,'34.123.139.117','-1',1601200343200),(21,'18.237.23.235','34.121.219.89','34.123.139.117','ip-172-31-11-100','us-west-2','hestia-us-central1-c-server','noca-not1',131670,68652,91,130182,67703,130109,67319,-1,-1,-1,'34.123.139.117','-1',1601200555880),(22,'18.237.23.235','34.121.219.89','34.123.139.117','ip-172-31-11-100','us-west-2','hestia-us-central1-c-server','noca-not1',129349,66689,0,129113,65918,128336,65668,-1,-1,-1,'34.123.139.117','-1',1601200555880),(23,'18.237.23.235','34.121.219.89','34.123.139.117','ip-172-31-11-100','us-west-2','hestia-us-central1-c-server','noca-not1',129479,67566,0,128449,65788,128358,65533,-1,-1,-1,'34.123.139.117','-1',1601200555880),(24,'18.237.23.235','34.121.219.89','34.123.139.117','ip-172-31-11-100','us-west-2','hestia-us-central1-c-server','noca-not1',129883,67175,0,129003,66598,128518,65749,-1,-1,-1,'34.123.139.117','-1',1601200555880),(25,'18.237.23.235','34.121.219.89','34.123.139.117','ip-172-31-11-100','us-west-2','hestia-us-central1-c-server','noca-not1',129956,67893,0,128657,65799,129106,66240,-1,-1,-1,'34.123.139.117','-1',1601200555880),(26,'15.165.70.216','34.87.222.191','35.221.191.94','ip-172-31-16-235','ap-northeast-2','hestia-australia-southeast1-c-server','noca-not1',-1,-1,161,137966,70030,324532,163189,-1,-1,-1,'-1','-1',1601200657910),(27,'18.183.238.70','104.199.219.205','35.221.191.94','ip-172-31-44-94','ap-northeast-1','hestia-asia-east1-c-server','noca-not1',84394,44580,82,80970,41215,80854,41292,-1,-1,-1,'35.221.191.94','-1',1601200684087),(28,'15.165.70.216','34.87.222.191','35.221.191.94','ip-172-31-16-235','ap-northeast-2','hestia-australia-southeast1-c-server','noca-not1',-1,-1,0,136719,69376,321629,160510,-1,-1,-1,'-1','-1',1601200657910),(29,'18.183.238.70','104.199.219.205','35.221.191.94','ip-172-31-44-94','ap-northeast-1','hestia-asia-east1-c-server','noca-not1',82515,42836,0,81454,41523,82036,42437,-1,-1,-1,'35.221.191.94','-1',1601200684087),(30,'15.165.70.216','34.87.222.191','35.221.191.94','ip-172-31-16-235','ap-northeast-2','hestia-australia-southeast1-c-server','noca-not1',-1,-1,0,135966,69309,321233,160237,-1,-1,-1,'-1','-1',1601200657910),(31,'13.235.57.112','34.95.45.42','35.221.191.94','ip-172-31-26-150','ap-south-1','hestia-northamerica-northeast1-c-server','noca-not1',401138,292936,142,218257,109245,480734,241922,-1,-1,-1,'35.221.191.94','-1',1601200619913),(32,'18.183.238.70','104.199.219.205','35.221.191.94','ip-172-31-44-94','ap-northeast-1','hestia-asia-east1-c-server','noca-not1',82113,43251,0,80634,41023,81930,43225,-1,-1,-1,'35.221.191.94','-1',1601200684087),(33,'15.165.70.216','34.87.222.191','35.221.191.94','ip-172-31-16-235','ap-northeast-2','hestia-australia-southeast1-c-server','noca-not1',-1,-1,0,137716,69868,321972,160754,-1,-1,-1,'-1','-1',1601200657910),(34,'13.235.57.112','34.95.45.42','35.221.191.94','ip-172-31-26-150','ap-south-1','hestia-northamerica-northeast1-c-server','noca-not1',396709,288277,0,217193,109093,480336,241568,-1,-1,-1,'35.221.191.94','-1',1601200619913),(35,'18.183.238.70','104.199.219.205','35.221.191.94','ip-172-31-44-94','ap-northeast-1','hestia-asia-east1-c-server','noca-not1',84040,43622,0,80563,40910,82975,43265,-1,-1,-1,'35.221.191.94','-1',1601200684087),(36,'15.165.70.216','34.87.222.191','35.221.191.94','ip-172-31-16-235','ap-northeast-2','hestia-australia-southeast1-c-server','noca-not1',-1,-1,0,135714,68855,321601,160327,-1,-1,-1,'-1','-1',1601200657910),(37,'13.235.57.112','34.95.45.42','35.221.191.94','ip-172-31-26-150','ap-south-1','hestia-northamerica-northeast1-c-server','noca-not1',397914,289763,0,217260,109037,480256,241566,-1,-1,-1,'35.221.191.94','-1',1601200619913),(38,'18.183.238.70','104.199.219.205','35.221.191.94','ip-172-31-44-94','ap-northeast-1','hestia-asia-east1-c-server','noca-not1',82053,42442,0,81071,42168,82478,42857,-1,-1,-1,'35.221.191.94','-1',1601200684087),(39,'13.235.57.112','34.95.45.42','35.221.191.94','ip-172-31-26-150','ap-south-1','hestia-northamerica-northeast1-c-server','noca-not1',397026,288724,0,218357,108792,481115,241753,-1,-1,-1,'35.221.191.94','-1',1601200619913),(40,'13.235.57.112','34.95.45.42','35.221.191.94','ip-172-31-26-150','ap-south-1','hestia-northamerica-northeast1-c-server','noca-not1',397649,288558,0,219285,109837,481765,242896,-1,-1,-1,'35.221.191.94','-1',1601200619913),(41,'13.239.112.40','34.87.222.191','34.87.242.250','ip-172-31-15-181','ap-southeast-2','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,8,11465,7208,11135,6818,-1,-1,-1,'-1','-1',1601200931308),(42,'13.239.112.40','34.87.222.191','34.87.242.250','ip-172-31-15-181','ap-southeast-2','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,11454,7092,10847,5967,-1,-1,-1,'-1','-1',1601200931308),(43,'13.239.112.40','34.87.222.191','34.87.242.250','ip-172-31-15-181','ap-southeast-2','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,10137,5112,10230,5607,-1,-1,-1,'-1','-1',1601200931308),(44,'13.239.112.40','34.87.222.191','34.87.242.250','ip-172-31-15-181','ap-southeast-2','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,9789,5233,10562,6113,-1,-1,-1,'-1','-1',1601200931308),(45,'13.239.112.40','34.87.222.191','34.87.242.250','ip-172-31-15-181','ap-southeast-2','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,9942,5559,9986,5468,-1,-1,-1,'-1','-1',1601200931308),(46,'54.179.194.255','104.199.219.205','35.221.191.94','ip-172-31-24-207','ap-southeast-1','hestia-asia-east1-c-server','auia-sot1',111625,58940,119,105766,53528,105419,53015,-1,-1,-1,'35.221.191.94','-1',1601200981871),(47,'54.179.194.255','104.199.219.205','35.221.191.94','ip-172-31-24-207','ap-southeast-1','hestia-asia-east1-c-server','auia-sot1',108257,56413,0,105351,53110,105107,52978,-1,-1,-1,'35.221.191.94','-1',1601200981871),(48,'18.177.136.175','34.87.222.191','35.221.191.94','ip-172-31-47-87','ap-northeast-1','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,47,82536,40423,283518,142466,-1,-1,-1,'-1','-1',1601201012802),(49,'15.222.63.70','34.95.45.42','35.203.28.222','ip-172-31-24-198','ca-central-1','hestia-northamerica-northeast1-c-server','auia-sot1',12060,8712,115,7629,4285,7339,3946,-1,-1,-1,'35.203.28.222','-1',1601201029926),(50,'54.179.194.255','104.199.219.205','35.221.191.94','ip-172-31-24-207','ap-southeast-1','hestia-asia-east1-c-server','auia-sot1',108053,56752,0,107261,54884,105099,52867,-1,-1,-1,'35.221.191.94','-1',1601200981871),(51,'18.177.136.175','34.87.222.191','35.221.191.94','ip-172-31-47-87','ap-northeast-1','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,82244,40197,283963,142257,-1,-1,-1,'-1','-1',1601201012802),(52,'15.222.63.70','34.95.45.42','35.203.28.222','ip-172-31-24-198','ca-central-1','hestia-northamerica-northeast1-c-server','auia-sot1',8775,6548,0,7127,3613,7296,3736,-1,-1,-1,'35.203.28.222','-1',1601201029926),(53,'54.179.194.255','104.199.219.205','35.221.191.94','ip-172-31-24-207','ap-southeast-1','hestia-asia-east1-c-server','auia-sot1',108135,56696,0,105188,52983,105533,53176,-1,-1,-1,'35.221.191.94','-1',1601200981871),(54,'18.177.136.175','34.87.222.191','35.221.191.94','ip-172-31-47-87','ap-northeast-1','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,82354,40267,283575,142661,-1,-1,-1,'-1','-1',1601201012802),(55,'15.222.63.70','34.95.45.42','35.203.28.222','ip-172-31-24-198','ca-central-1','hestia-northamerica-northeast1-c-server','auia-sot1',8425,5086,0,8507,4742,6704,3571,-1,-1,-1,'35.203.28.222','-1',1601201029926),(56,'54.179.194.255','104.199.219.205','35.221.191.94','ip-172-31-24-207','ap-southeast-1','hestia-asia-east1-c-server','auia-sot1',108483,57133,0,105465,52996,105624,53757,-1,-1,-1,'35.221.191.94','-1',1601200981871),(57,'18.177.136.175','34.87.222.191','35.221.191.94','ip-172-31-47-87','ap-northeast-1','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,83090,40982,282784,141827,-1,-1,-1,'-1','-1',1601201012802),(58,'15.222.63.70','34.95.45.42','35.203.28.222','ip-172-31-24-198','ca-central-1','hestia-northamerica-northeast1-c-server','auia-sot1',8519,4824,0,7054,3652,8035,5303,-1,-1,-1,'35.203.28.222','-1',1601201029926),(59,'18.177.136.175','34.87.222.191','35.221.191.94','ip-172-31-47-87','ap-northeast-1','hestia-australia-southeast1-c-server','auia-sot1',-1,-1,0,82215,40204,283176,142099,-1,-1,-1,'-1','-1',1601201012802),(60,'15.222.63.70','34.95.45.42','35.203.28.222','ip-172-31-24-198','ca-central-1','hestia-northamerica-northeast1-c-server','auia-sot1',8562,5278,1,6928,3641,7460,4086,-1,-1,-1,'35.203.28.222','-1',1601201029926),(61,'35.158.103.110','35.228.26.105','35.228.62.197','ip-172-31-6-217','eu-central-1','hestia-europe-north1-c-server','auia-sot1',69805,37083,4,64893,33136,64107,31899,-1,-1,-1,'35.228.62.197','-1',1601201205767),(62,'35.158.103.110','35.228.26.105','35.228.62.197','ip-172-31-6-217','eu-central-1','hestia-europe-north1-c-server','auia-sot1',66010,33659,0,64776,32516,64165,32032,-1,-1,-1,'35.228.62.197','-1',1601201205767),(63,'52.50.155.255','34.95.45.42','35.228.62.197','ip-172-31-45-227','eu-west-1','hestia-northamerica-northeast1-c-server','auia-sot1',180258,133483,19,97663,50614,176322,88509,-1,-1,-1,'35.228.62.197','-1',1601201214692),(64,'35.158.103.110','35.228.26.105','35.228.62.197','ip-172-31-6-217','eu-central-1','hestia-europe-north1-c-server','auia-sot1',66090,34338,0,65456,33174,64649,32307,-1,-1,-1,'35.228.62.197','-1',1601201205767),(65,'52.50.155.255','34.95.45.42','35.228.62.197','ip-172-31-45-227','eu-west-1','hestia-northamerica-northeast1-c-server','auia-sot1',176362,130029,0,97901,50633,178145,88773,-1,-1,-1,'35.228.62.197','-1',1601201214692),(66,'35.158.103.110','35.228.26.105','35.228.62.197','ip-172-31-6-217','eu-central-1','hestia-europe-north1-c-server','auia-sot1',65822,33465,0,64807,32599,65719,33425,-1,-1,-1,'35.228.62.197','-1',1601201205767),(67,'52.50.155.255','34.95.45.42','35.228.62.197','ip-172-31-45-227','eu-west-1','hestia-northamerica-northeast1-c-server','auia-sot1',176916,130502,0,97487,50266,178261,88489,-1,-1,-1,'35.228.62.197','-1',1601201214692),(68,'35.180.116.229','34.121.219.89','35.228.62.197','ip-172-31-39-158','eu-west-3','hestia-us-central1-c-server','auia-sot1',180794,143230,2,77833,40176,211156,106440,-1,-1,-1,'35.228.62.197','-1',1601201236625),(69,'35.158.103.110','35.228.26.105','35.228.62.197','ip-172-31-6-217','eu-central-1','hestia-europe-north1-c-server','auia-sot1',66747,35346,0,65438,32854,64521,32875,-1,-1,-1,'35.228.62.197','-1',1601201205767),(70,'52.50.155.255','34.95.45.42','35.228.62.197','ip-172-31-45-227','eu-west-1','hestia-northamerica-northeast1-c-server','auia-sot1',176337,130037,0,96622,49768,177296,88253,-1,-1,-1,'35.228.62.197','-1',1601201214692),(71,'35.180.116.229','34.121.219.89','35.228.62.197','ip-172-31-39-158','eu-west-3','hestia-us-central1-c-server','auia-sot1',177423,140143,0,84504,46777,209112,104980,-1,-1,-1,'35.228.62.197','-1',1601201236625),(72,'35.178.190.171','34.95.45.42','35.228.62.197','ip-172-31-1-101','eu-west-2','hestia-northamerica-northeast1-c-server','auia-sot1',156916,119940,8,77899,40300,161798,81713,-1,-1,-1,'35.228.62.197','-1',1601201227777),(73,'52.50.155.255','34.95.45.42','35.228.62.197','ip-172-31-45-227','eu-west-1','hestia-northamerica-northeast1-c-server','auia-sot1',176422,129972,0,96210,48944,177475,88176,-1,-1,-1,'35.228.62.197','-1',1601201214692),(74,'35.180.116.229','34.121.219.89','35.228.62.197','ip-172-31-39-158','eu-west-3','hestia-us-central1-c-server','auia-sot1',177876,140367,0,77341,39682,210878,106777,-1,-1,-1,'35.228.62.197','-1',1601201236625),(75,'35.178.190.171','34.95.45.42','35.228.62.197','ip-172-31-1-101','eu-west-2','hestia-northamerica-northeast1-c-server','auia-sot1',153920,116865,0,77590,40201,161557,81884,-1,-1,-1,'35.228.62.197','-1',1601201227777),(76,'35.180.116.229','34.121.219.89','35.228.62.197','ip-172-31-39-158','eu-west-3','hestia-us-central1-c-server','auia-sot1',177283,138785,0,76792,38591,209263,105075,-1,-1,-1,'35.228.62.197','-1',1601201236625),(77,'35.178.190.171','34.95.45.42','35.228.62.197','ip-172-31-1-101','eu-west-2','hestia-northamerica-northeast1-c-server','auia-sot1',154347,117492,0,78170,40350,162230,81010,-1,-1,-1,'35.228.62.197','-1',1601201227777),(78,'35.180.116.229','34.121.219.89','35.228.62.197','ip-172-31-39-158','eu-west-3','hestia-us-central1-c-server','auia-sot1',177498,140442,0,76904,38679,209794,105199,-1,-1,-1,'35.228.62.197','-1',1601201236625),(79,'35.178.190.171','34.95.45.42','35.228.62.197','ip-172-31-1-101','eu-west-2','hestia-northamerica-northeast1-c-server','auia-sot1',154881,116914,0,77207,39841,161570,81047,-1,-1,-1,'35.228.62.197','-1',1601201227777),(80,'35.178.190.171','34.95.45.42','35.228.62.197','ip-172-31-1-101','eu-west-2','hestia-northamerica-northeast1-c-server','auia-sot1',154726,116916,0,78423,39855,161345,81049,-1,-1,-1,'35.228.62.197','-1',1601201227777);
/*!40000 ALTER TABLE `transfer_time` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-27 10:21:13
