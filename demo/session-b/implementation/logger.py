"""
日誌模組 (Logger Module) - Python實現

根據規格文件實現，未參考原程式碼實現
Session B：移植開發者角色
"""

from datetime import datetime
from enum import IntEnum
from pathlib import Path


class LogLevel(IntEnum):
    """日誌等級定義"""
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3


class Logger:
    """
    日誌記錄器
    
    根據規格文件實現：
    -支援四個日誌等級：DEBUG, INFO, WARN, ERROR
    -等級過濾：只記錄等級 >=最小等級的日誌
    -日誌格式：[時間戳記] 等級: 訊息
    -寫入日誌檔案
    """
    
    def __init__(self, log_file: str = 'app.log', min_level: LogLevel = LogLevel.INFO):
        """
        初始化日誌記錄器
        
        Args:
            log_file: 日誌檔案路徑（預設 'app.log'）
            min_level: 最小日誌等級（預設 INFO）
        """
        self._log_file = log_file
        self._min_level = min_level
        self._ensure_log_file()
    
    def _ensure_log_file(self):
        """確保日誌檔案存在（若不存在則建立）"""
        Path(self._log_file).touch(exist_ok=True)
    
    def _format_timestamp(self) -> str:
        """
        格式化時間戳記
        
        Returns:
            ISO 格式時間戳記：YYYY-MM-DD HH:mm:ss
        """
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
    
    def _write_log(self, level: LogLevel, message: str) -> bool:
        """
        寫入日誌
        
        Args:
            level: 日誌等級
            message: 日誌訊息
        
        Returns:
            bool: 是否成功寫入
        """
        #等級過濾：低於最小等級則不記錄
        if level < self._min_level:
            return False
        
        #格式化日誌內容
        timestamp = self._format_timestamp()
        level_name = level.name
        log_line = f'[{timestamp}] {level_name}: {message}\n'
        
        #寫入檔案
        try:
            with open(self._log_file, 'a', encoding='utf-8') as f:
                f.write(log_line)
            return True
        except IOError as e:
            #寫入失敗時輸出錯誤到控制台
            print(f'日誌寫入失敗: {e}')
            return False
    
    def debug(self, message: str) -> bool:
        """記錄 DEBUG等級日誌"""
        return self._write_log(LogLevel.DEBUG, message)
    
    def info(self, message: str) -> bool:
        """記錄 INFO等級日誌"""
        return self._write_log(LogLevel.INFO, message)
    
    def warn(self, message: str) -> bool:
        """記錄 WARN等級日誌"""
        return self._write_log(LogLevel.WARN, message)
    
    def error(self, message: str) -> bool:
        """記錄 ERROR等級日誌"""
        return self._write_log(LogLevel.ERROR, message)
    
    def set_min_level(self, level: LogLevel) -> bool:
        """
       設定最小日誌等級
        
        Args:
            level: 新的最小等級
        
        Returns:
            bool: 是否成功設定
        """
        if level in LogLevel:
            self._min_level = level
            return True
        return False
    
    def get_min_level(self) -> LogLevel:
        """取得當前最小日誌等級"""
        return self._min_level


#模組匯出
__all__ = ['Logger', 'LogLevel']