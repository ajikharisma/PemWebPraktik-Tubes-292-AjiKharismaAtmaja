-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 05, 2025 at 10:03 AM
-- Server version: 8.0.30
-- PHP Version: 8.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugasbesar_pwp`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `username` varchar(64) NOT NULL,
  `email` varchar(120) NOT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'user',
  `password_hash` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `role`, `password_hash`) VALUES
(1, 'saya', 'adminganteng@gmail.com', 'user', 'scrypt:32768:8:1$9zLuPIaytGd9y1zC$ddfdddde8909f0277b7bbc9c67ea2111b4c1d4430e8f750ca7339fa7051a08faaa080fbb5f2c42070858addb2621356ec11292fab3d80c8ce2a73f5e75f72691'),
(7, 'jojo', 'jojo@gmail.com', 'user', 'scrypt:32768:8:1$QR9LMJZqDgXcqCrj$eecfb1738e3f220947c84d1d687fc70022fcd1d2920e8a84a11ed5b9c6fca8293611709122ec432a3828abe4e5bd3bc13067316f54e8d8a0d7d37c59efd7cd94'),
(10, 'bayu', 'bayunihbos@gmail.com', 'user', 'scrypt:32768:8:1$AOzuzH1oaMRr7vTk$4cfddc84006493538464b22b6601b22e090ec8b921054cf241f57d54355bee04fb78f632ca0b0a433bd75cb73eb10a773d870fa472edb7a3a438551337f9c68e'),
(13, 'joko', 'joko@gmail.com', 'user', 'scrypt:32768:8:1$x8eXMdazB7HXfXmM$abbcaa497f7ae0ff2a615aa15dd036414be205b096d52d18aa10041c83e0469febd578d4df9e548e472e61eb84892b873f919e0bb0bcfad1a1717beab9a06f06'),
(14, 'kamu', 'kamu@gmail.com', 'user', 'scrypt:32768:8:1$vwW76SFo5iWduiIA$81c581df90b34b93db779742af49093befe1d546223467b6d9e9e22ac254b4c47948c3bb91ff53e9734c4a9d60e337c5197502bb947a91a56e57743051ce3b43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
