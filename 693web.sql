/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : localhost:3306
 Source Schema         : web

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : 65001

 Date: 08/08/2024 15:18:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for web_active
-- ----------------------------
DROP TABLE IF EXISTS `web_active`;
CREATE TABLE `web_active`  (
  `id` int(11) NOT NULL,
  `active_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '活动名称',
  `active_time` datetime NOT NULL COMMENT '活动时间',
  `user_id` int(11) NULL DEFAULT NULL COMMENT '创建用户',
  `admin_id` int(11) NULL DEFAULT NULL COMMENT '创建管理员',
  `user_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户名称',
  `admin_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建管理员名称',
  `active_location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '活动地点',
  `active_desc` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '活动详情(富文本)',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '状态1可用,0删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_active
-- ----------------------------
INSERT INTO `web_active` VALUES (0, '海滩派对', '2024-08-08 14:34:45', 1, 0, NULL, NULL, '海滩', '海滩上面开排队', '1');

-- ----------------------------
-- Table structure for web_active_kind
-- ----------------------------
DROP TABLE IF EXISTS `web_active_kind`;
CREATE TABLE `web_active_kind`  (
  `id` int(11) NOT NULL,
  `active_id` int(11) NOT NULL COMMENT '活动id',
  `kind_id` int(11) NOT NULL COMMENT '用户id',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '状态:1关联2取消',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '参加的活动' ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of web_active_kind
-- ----------------------------
INSERT INTO `web_active_kind` VALUES (1, 1, 1, '1');

-- ----------------------------
-- Table structure for web_active_user
-- ----------------------------
DROP TABLE IF EXISTS `web_active_user`;
CREATE TABLE `web_active_user`  (
  `id` int(11) NOT NULL,
  `active_id` int(11) NOT NULL COMMENT '活动id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '状态:1注册2取消',
  `create_time` datetime NOT NULL COMMENT '注册时间',
  `type` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '1:参加,2:收藏',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '参加的活动' ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of web_active_user
-- ----------------------------

-- ----------------------------
-- Table structure for web_admin
-- ----------------------------
DROP TABLE IF EXISTS `web_admin`;
CREATE TABLE `web_admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `login` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '登录账号',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `login_time` datetime NULL DEFAULT NULL COMMENT '`',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '1:启用,0禁用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '管理员' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_admin
-- ----------------------------
INSERT INTO `web_admin` VALUES (1, 'name', 'login', '123456', '2024-08-08 14:33:50', '1');

-- ----------------------------
-- Table structure for web_kind
-- ----------------------------
DROP TABLE IF EXISTS `web_kind`;
CREATE TABLE `web_kind`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kind_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '类别名称',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '状态:1可用,0禁用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '活动类别标签' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_kind
-- ----------------------------
INSERT INTO `web_kind` VALUES (1, '派对', '1');

-- ----------------------------
-- Table structure for web_user
-- ----------------------------
DROP TABLE IF EXISTS `web_user`;
CREATE TABLE `web_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `login` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '登录账号',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `login_time` datetime NULL DEFAULT NULL COMMENT '`',
  `status` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '1:启用,0禁用',
  `pic` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  `desc` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '简介',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_user
-- ----------------------------
INSERT INTO `web_user` VALUES (1, 'user', 'login', '123456', '2024-08-08 14:34:18', '1', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
