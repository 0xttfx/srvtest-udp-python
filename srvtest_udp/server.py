import asyncio

class UDPServerProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        """
        Método chamado quando a conexão é estabelecida.
        Aqui, 'transport' representa o canal de comunicação UDP.
        """
        self.transport = transport
        print('Servidor UDP iniciado. Aguardando datagramas...')

    def datagram_received(self, data, addr):
        """
        Método chamado sempre que um novo datagrama (pacote UDP) é recebido.
        'data' é o conteúdo recebido e 'addr' é o endereço do remetente.
        """
        # Decodifica os dados recebidos (assumindo codificação UTF-8)
        message = data.decode('utf-8', errors='ignore')
        print(f"Recebido: {message} de {addr}")

        # Cria uma tarefa assíncrona para processar a mensagem sem bloquear o recebimento de novos datagramas
        asyncio.create_task(self.process_message(message, addr))

    async def process_message(self, message, addr):
        """
        Função assíncrona para processar a mensagem recebida.
        Esse processamento pode incluir operações I/O (por exemplo, escrita em log, consulta a banco de dados, etc.).
        """
        print(f"Iniciando processamento da mensagem de {addr}")
        # Simula uma operação I/O com await (por exemplo, acesso a banco de dados ou escrita em log)
        await asyncio.sleep(1)  # Simulação de atraso para operações assíncronas

        # Após o processamento, envia uma resposta ao cliente (opcional)
        response = f"Mensagem '{message}' processada com sucesso!".encode('utf-8')
        self.transport.sendto(response, addr)
        print(f"Resposta enviada para {addr}")

async def main():
    """
    Função principal que configura e inicia o servidor UDP.
    """
    # Obtém o loop de eventos assíncrono atual
    loop = asyncio.get_running_loop()

    # Cria um endpoint UDP que escuta em todas as interfaces na porta 9999
    print("Iniciando o servidor UDP na porta 9999...")
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPServerProtocol(),
        local_addr=('0.0.0.0', 9999)
    )

    try:
        # Mantém o servidor ativo; nesse exemplo, ele ficará ativo indefinidamente.
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        # Permite o encerramento do servidor via Ctrl+C
        print("Encerrando o servidor UDP...")
    finally:
        # Fecha o canal de comunicação ao finalizar
        transport.close()

if __name__ == '__main__':
    # Inicia o loop de eventos assíncrono e executa a função main()
    asyncio.run(main())

