# vllm_template

- [vllm\_template](#vllm_template)
  - [目錄架構](#目錄架構)
  - [環境設定](#環境設定)
  - [系統執行](#系統執行)

## 目錄架構
```
.
├── src                                - source code
├── poetry.lock                        - poetry 環境相關文檔
├── pyproject.toml                     - poetry 依賴的 package 及版本
├── README.md                          - 說明文件
└── requirements.txt                   - pip 依賴的 package 及版本
```


## 環境設定

- 套件管理 
    - poetry [使用指南](https://blog.kyomind.tw/python-poetry/)
        - 安裝 pyproject.toml 裡的套件
            ```bash
            poetry install --no-root
            ```
        - 進入環境
            ```bash
            poetry shell
            ```
        - 退出環境
            ```bash
            exit
            ```
        - 新增套件
            ```bash
            poetry add [Package]
            ```
        - 移除套件
            ```bash
            poetry remove [Package]
            ```
        - 匯出 requirements.txt
            ```bash
            poetry export -f requirements.txt -o requirements.txt --without-hashes --dev
            ```
    - pip
        - 安裝 requirements.txt 裡的套件
            ```bash
            pip install -r requirements.txt
            ```


## 系統執行

- 執行
  - 啟動服務器
      ```bash
      python src/server.py
      ```
  - 測試服務
      ```bash
      python src/test_client.py
      ```
