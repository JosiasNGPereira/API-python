import datetime
import logging
import azure.functions as func
from api_in import produto_plano_de_contas

CACHED_DATA = None
obj3 = "produto_plano_de_contas"
url_base = os.getenv('DB_UR')
cont_pg = 0
url_tg = f"{url_base}/{obj3}?cursor={cont_pg}"
def verificar_API(dados):
    
    if dados is not None:
        if len(dados) > 0:
            for estrutura in dados:
                print(estrutura)
        else:
            print("Nenhum dado encontrado.")
    else:
        print("Falha ao acessar a API.")
        
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    global CACHED_DATA
    if CACHED_DATA is None:
        CACHED_DATA = load_json()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
    produto_plano_de_contas()
    
    dados = produto_plano_de_contas(url_tg)
    print(logging.info)
    print("Teste Azure passou aqui no main ")
             
    
if __name__ == "__main__":
    # Simulando um objeto TimerRequest para teste local
    class FakeTimerRequest:
        past_due = False
    
    fake_timer = FakeTimerRequest()
    
    print("Teste Azure passou aqui FORA DO MAIN ")
    main(fake_timer)