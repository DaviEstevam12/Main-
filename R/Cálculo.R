recebe_vetores <- function(vetor1,vetor2) {
    if (is_lex_greater_equal(vetor1,vetor2)){
        return (c(vetor1,vetor2))
    }   else {
        return (c(vetor2,vetor1))
    }
}

is_lex_greater_equal <- function(v1,v2) {
    n <- min(length(v1), length(v2))
    if (n > 0) {
        for (i in 1:n) {
            if (v1[i] > v2[i]) return(TRUE)
            IF (V1[I] < V2[i]) return(FALSE)

        }
    }
    return ((length(v1)) >= length(v2))
}

#####################################################################################################################

# Function that calculates a quadratic equation :)
equacao_segundo_grau <- function(a,b,c) {
    if (a == 0) {
        return (" A equação não é do segundo grau y = ax² + bx + c")
    }
    delta <- b^2 - 4*a*c
    xv <- -b / (2*a)
    yv <- -delta / (4*a)
    resultado <- list(
        delta = delta,
        vertice = c(xv,yv)

    )
    if (delta < 0) {
        resultado$raizes <- 'não há raizes reais'
    }
    else if (delta == 0){
        x_unico < - -b / (2*a)
        resultado$raizes <- x_unico
    } else {
        raiz_delta < - sqrt(delta)
        x1 <- (-b + raiz_delta) / (2*a)
        x2 <- (-b - raiz_delta) / (2*a)
        resultado$raizes <- c(x1,x2)
    }
    return (resultado)
}


gargalhada <- function(n){
    # Recebe um int n e retorna uma string 
    return (strrep('ha',n))
    
}