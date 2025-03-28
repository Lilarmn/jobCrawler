USE [master]
GO
/****** Object:  Database [CrawlData]    Script Date: 2/10/2024 12:59:06 AM ******/
CREATE DATABASE [CrawlData]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'CrawlData', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\CrawlData.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'CrawlData_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\CrawlData_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [CrawlData] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CrawlData].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [CrawlData] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [CrawlData] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [CrawlData] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [CrawlData] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [CrawlData] SET ARITHABORT OFF 
GO
ALTER DATABASE [CrawlData] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [CrawlData] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [CrawlData] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [CrawlData] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [CrawlData] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [CrawlData] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [CrawlData] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [CrawlData] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [CrawlData] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [CrawlData] SET  ENABLE_BROKER 
GO
ALTER DATABASE [CrawlData] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [CrawlData] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [CrawlData] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [CrawlData] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [CrawlData] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [CrawlData] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [CrawlData] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [CrawlData] SET RECOVERY FULL 
GO
ALTER DATABASE [CrawlData] SET  MULTI_USER 
GO
ALTER DATABASE [CrawlData] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [CrawlData] SET DB_CHAINING OFF 
GO
ALTER DATABASE [CrawlData] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [CrawlData] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [CrawlData] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [CrawlData] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'CrawlData', N'ON'
GO
ALTER DATABASE [CrawlData] SET QUERY_STORE = OFF
GO
USE [CrawlData]
GO
/****** Object:  Table [dbo].[jobinja]    Script Date: 2/10/2024 12:59:06 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[jobinja](
	[company] [nvarchar](max) NULL,
	[title] [nvarchar](max) NULL,
	[location] [nvarchar](max) NULL,
	[category] [nvarchar](max) NULL,
	[essentials] [nvarchar](max) NULL,
	[salary] [nvarchar](max) NULL,
	[experience] [nvarchar](max) NULL,
	[type_of_work] [nvarchar](max) NULL,
	[studies] [nvarchar](max) NULL,
	[military] [nvarchar](max) NULL,
	[gender] [nvarchar](max) NULL,
	[description] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[jobinja_companies]    Script Date: 2/10/2024 12:59:06 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[jobinja_companies](
	[link] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [CrawlData] SET  READ_WRITE 
GO
