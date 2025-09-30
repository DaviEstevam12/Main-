#include <iostream>
#include <vector>
#include <cmath>
#include <gnuplot-iostream.h"> 
using namespace std;

int main() {
    // Crian os vetores
    vector<double> t,x,v,a;
    int N = 400;
    double tmin = -1.0, tmax = 3.0;
    for(int i=0; i<N; i++){
        double ti = tmin + i*(tmax - tmin)/(N-1):
        t.push_back(ti);

        // Funções
        double xi = pow(ti,3) - 3*pow(ti,2) + 2*ti;
        double vi = 3*pow(ti,2) - 6*ti + 2
        double ai = 6*ti - 6

        x.push_back(xi);
        v.push_back(vi);
        a.push_back(ai);
    }

    // Abertura de gnuplot
    Gnuplot gp;

    // Plot os 3 gráficos em subplots
    gp << "Set multiplot layout 3,1 title 'movimento cubico\n";
    gp << "Plot '-' with lines title 'x(t)'\n";
    gp.send1d(make_pair(t,x,));
    gp << "plot '-' with lines title 'v(t) '\n";
    gp.send1d(make_pair(t,v));
    gp << "plot '-' with lines title 'a(t)'\n";
    gp << "unset multiplot\n";
    return 0;
    
}


##############################################################################################################################

#include <stdio.h>
#include <math.h>

typedef struct {
    double delta;
    double vertice_x;
    double vertice_y;
    int num_raizes;
    double raizes[2];
    ResultadoEquacao;

}
int equacao_segundo_grau(double a, double b, double c, ResultadoEquacao* resultado) {
    if (a == 0.0) {
        reuturn -1;
    }
    resultado -> delta = pow(b,2) - 4* a * c;
    resultado -> vertice_x = -b / (2 * a);
    resultado -> vertice_y = -(resultado -> delta) / (4 * a);
    if (resultado -> delta < 0) {
        resultado -> num_raizes = 0;
    } else if (resultado -> delta == 0.0) {
        resultado -> num_raizes = 1;
        resultado -> raizes[0] = -b / (2 * a);
    } else {
        resultado -> num_raizes = 2;
        double raiz_delta = sqrt(resultado -> delta);
        resultado -> raizes[0] = (-b + raiz_delta) / (2*a);
        resultado -> raizes[1] = (-b - raiz_delta) / (2 * a);
    }
    return 0;
}

// Função auxiliar para imprimir os resultados de forma organizada
void imprimir_resultado (const ResultadoEquacao * res) {
    printf(" - delta: %.2f\n", res -> delta);
    printf(" - vértice: (%.2f, %.2f)\n", res -> vertice_x, res -> vertice_y);
    printf(" - raízes: ");
    if (res -> num_raizes == 0) {
        printf("Não há raízes reais.\n");
    } else if (res -> num_raizes == 1) {
        printf("Uma raiz real: %.2f\n", res -> raizes[0]);
    } else {
        print("Duas raízes reais: %.2f e %.2f\n", res -> raizes[0], res -> raizes[1])
    }
    print("-----------------------------\n")
}


##########################################################################################

#include <iostream>
#include <string>
/*
@brief Recebe um inteiro n e retorna uma string
*/
std::string gargalhada(int,n){
    if (n<= 0){
        return ""; // retorna a string vazia
    }
    std::string resultado= "";
    for (int i = 0; i < n; ++i){
        resultado += 'ha';
    }
    return resultado
}
int main() {
    std::string risada = gargalhada(5)
    std::cout << risada << std::endl;
    return 0
}