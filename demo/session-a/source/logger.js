/**
 * 日誌模組 (Logger Module)
 * 
 * 功能：將程式執行過程中的重要事件記錄到檔案
 */

const fs = require('fs');
const path = require('path');

//日誌等級定義
const LogLevel = {
  DEBUG: 0,
  INFO: 1,
  WARN: 2,
  ERROR: 3
};

//預設配置
const DEFAULT_CONFIG = {
  logFile: 'app.log',
  minLevel: LogLevel.INFO,
  dateFormat: 'YYYY-MM-DD HH:mm:ss'
};

/**
 * 日誌記錄器類別
 */
class Logger {
  constructor(config = {}) {
    this.config = {...DEFAULT_CONFIG, ...config };
    this.logFile = this.config.logFile;
    this.minLevel = this.config.minLevel;
  }

  /**
   * 格式化時間戳記
   */
  _formatTimestamp() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  }

  /**
   * 取得日誌等級名稱
   */
  _getLevelName(level) {
    const names = ['DEBUG', 'INFO', 'WARN', 'ERROR'];
    return names[level] || 'UNKNOWN';
  }

  /**
   * 寫入日誌
   */
  _writeLog(level, message) {
    //等級過濾：低於最小等級則不記錄
    if (level < this.minLevel) {
      return false;
    }

    //格式化日誌內容
    const timestamp = this._formatTimestamp();
    const levelName = this._getLevelName(level);
    const logLine = `[${timestamp}] ${levelName}: ${message}\n`;

    //寫入檔案
    try {
      fs.appendFileSync(this.logFile, logLine, 'utf8');
      return true;
    } catch (err) {
      console.error('日誌寫入失敗:', err.message);
      return false;
    }
  }

  /**
   * DEBUG等級日誌
   */
  debug(message) {
    return this._writeLog(LogLevel.DEBUG, message);
  }

  /**
   * INFO等級日誌
   */
  info(message) {
    return this._writeLog(LogLevel.INFO, message);
  }

  /**
   * WARN等級日誌
   */
  warn(message) {
    return this._writeLog(LogLevel.WARN, message);
  }

  /**
   * ERROR等級日誌
   */
  error(message) {
    return this._writeLog(LogLevel.ERROR, message);
  }

  /**
   *設定最小日誌等級
   */
  setMinLevel(level) {
    if (level >= LogLevel.DEBUG && level <= LogLevel.ERROR) {
      this.minLevel = level;
      return true;
    }
    return false;
  }

  /**
   *取得當前最小日誌等級
   */
  getMinLevel() {
    return this.minLevel;
  }
}

//匯出模組
module.exports = { Logger, LogLevel };