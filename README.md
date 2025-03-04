# srvtest-udp-python
Servidor UDP em Python para testes

- Execução do servidor:

Para executar o servidor, basta rodar o script udp_server/server.py:

```python
python3 -m srvtest_udp.server
```

- Testes

Para rodar os testes, instale o pytest e pytest-asyncio (se ainda não estiverem instalados) e execute:

```bash
pip install pytest pytest-asyncio
pytest
``` 

- Instalação do pacote:

Você pode instalar o pacote localmente com
Isso permite que você importe e utilize o pacote conforme necessário.

```bash
pip install -e .
```
