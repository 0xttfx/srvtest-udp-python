import asyncio
import pytest
from udp_server.server import UDPServerProtocol

# Protocolo auxiliar para o cliente UDP utilizado no teste
class TestUDPClientProtocol(asyncio.DatagramProtocol):
    def __init__(self, message, on_response, loop):
        self.message = message.encode('utf-8')
        self.on_response = on_response
        self.loop = loop

    def connection_made(self, transport):
        self.transport = transport
        # Envia a mensagem assim que a conexão é estabelecida
        self.transport.sendto(self.message)

    def datagram_received(self, data, addr):
        # Define o resultado do futuro com a resposta recebida
        self.on_response.set_result(data.decode('utf-8'))
        self.transport.close()

    def error_received(self, exc):
        self.on_response.set_exception(exc)

@pytest.mark.asyncio
async def test_udp_server_response():
    loop = asyncio.get_running_loop()
    
    # Inicia o servidor UDP em uma porta de teste, por exemplo, 9998
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPServerProtocol(),
        local_addr=('127.0.0.1', 9998)
    )

    # Prepara um futuro para aguardar a resposta do servidor
    on_response = loop.create_future()
    test_message = "Teste"
    
    # Cria o cliente UDP que se conecta ao servidor de teste
    client_transport, client_protocol = await loop.create_datagram_endpoint(
        lambda: TestUDPClientProtocol(test_message, on_response, loop),
        remote_addr=('127.0.0.1', 9998)
    )

    # Aguarda a resposta com um timeout para evitar bloqueios no teste
    response = await asyncio.wait_for(on_response, timeout=3.0)
    
    # Verifica se a resposta contém a mensagem esperada
    assert "Mensagem 'Teste' processada com sucesso!" in response

    # Fecha os transportes para liberar a porta
    client_transport.close()
    transport.close()

