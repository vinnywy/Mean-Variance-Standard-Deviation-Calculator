# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

''' Função Criada com auxílio de IA para melhor clareza dos resultados obtidos 
def pretty_print(result):
    print("\n📊 Resultados da Análise da Matriz 3x3\n")
    for key, value in result.items():
        print(f"➡️ {key.capitalize()}:")
        print(f"   • Por coluna: {value[0]}")
        print(f"   • Por linha:  {value[1]}")
        print(f"   • Total:      {value[2]}\n")

if __name__ == "__main__":
    data = [0,1,2,3,4,5,6,7,8]
    result = mean_var_std.calculate(data)
    pretty_print(result)
'''

# Run unit tests automatically
main(module='test_module', exit=False)