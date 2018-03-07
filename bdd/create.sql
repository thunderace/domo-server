
-- mysql -u root -p < create.sql
-- sudo mysql -u root -p < create.sql
-- mysql -h localhost -u root -p < create.sql

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


CREATE DATABASE domo;
CREATE DATABASE teleinfo;

GRANT ALL PRIVILEGES ON domo.* TO 'domo'@'localhost' IDENTIFIED BY 'domo';
GRANT ALL PRIVILEGES ON domo.* TO 'domo'@'#' IDENTIFIED BY 'domo';
GRANT ALL PRIVILEGES ON teleinfo.* TO 'teleinfo'@'localhost' IDENTIFIED BY 'teleinfo';
GRANT ALL PRIVILEGES ON teleinfo.* TO 'teleinfo'@'#' IDENTIFIED BY 'teleinfo';

USE domo;

--
-- Database: `domo`
--

-- --------------------------------------------------------

--
-- Table structure for table `mqtt`
--

CREATE TABLE IF NOT EXISTS `mqtt` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `topic` varchar(100) DEFAULT NULL,
  `payload` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT AUTO_INCREMENT=209546 ;

-- --------------------------------------------------------


USE teleinfo;

--
-- Database: `teleinfo`
--

-- --------------------------------------------------------

--
-- Table structure for table `papp_inst`
--

CREATE TABLE IF NOT EXISTS `papp_inst` (
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ID_UNIQUE` tinyint(1) NOT NULL DEFAULT '1',
  `PAPP_INST` int(5) DEFAULT '-1',
  PRIMARY KEY (`time`),
  UNIQUE KEY `ID_UNIQUE` (`ID_UNIQUE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `teleinfo`
--

CREATE TABLE IF NOT EXISTS `teleinfo` (
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `OPTARIF` varchar(4) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `ISOUSC` tinyint(2) DEFAULT '0',
  `BASE` varchar(20) DEFAULT NULL,
  `IINST` tinyint(3) DEFAULT '0',
  `IMAX` tinyint(3) DEFAULT '0',
  `PAPP` int(5) DEFAULT '0',
  UNIQUE KEY `time` (`time`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
