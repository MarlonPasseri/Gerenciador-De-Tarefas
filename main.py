class GerenciadorTarefas:
  def __init__(self):
      self.tarefas = []

  def adicionar_tarefa(self, descricao):
      self.tarefas.append(descricao)
      print(f'Tarefa "{descricao}" adicionada com sucesso!')

  def excluir_tarefa(self, indice):
      try:
          tarefa_removida = self.tarefas.pop(indice)
          print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
      except IndexError:
          print('Índice inválido. A tarefa não foi removida.')

  def mostrar_tarefas(self):
      if not self.tarefas:
          print('Nenhuma tarefa encontrada.')
      else:
          print('Lista de tarefas:')
          for i, tarefa in enumerate(self.tarefas):
              print(f'{i + 1}. {tarefa}')

# Função principal
def main():
  gerenciador = GerenciadorTarefas()

  while True:
      print('\n==== Gerenciador de Tarefas ====')
      print('1. Adicionar Tarefa')
      print('2. Excluir Tarefa')
      print('3. Mostrar Tarefas')
      print('0. Sair')

      opcao = input('Escolha uma opção: ')

      if opcao == '1':
          descricao = input('Digite a descrição da tarefa: ')
          gerenciador.adicionar_tarefa(descricao)
      elif opcao == '2':
          indice = int(input('Digite o índice da tarefa a ser removida: '))
          gerenciador.excluir_tarefa(indice - 1)  # Subtrai 1 pois os índices começam em 1 para o usuário
      elif opcao == '3':
          gerenciador.mostrar_tarefas()
      elif opcao == '0':
          print('Saindo do gerenciador de tarefas. Até mais!')
          break
      else:
          print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
  main()

