using Plots
# Intervalo de tempo
t = range(-1, 3, length = 400)
# Posição
x = t.^3 .- 3.* t.^2 .+ 2.*t

# Velocidade 
v = 3.* t.^2 .- 6 .* t.+ 2

# Aceleração
a = 6 .*t .-6

# Criando os gráficos
plot(t, x, label="x(t) = t³ -3t² + 2t", color=:blue, lw=2, title="Posição")
plot!(t, zeros(length(t)), color=:black, lw=0.5, label="")
plot(t, v, label="v(t) = 3t² - 6t +2", color=:green, lw=2, title="velocidae")
plot!(t, zeros,(length(t)), color=:black, lw= 0.5, label="")
plot(t, a, label="a(t) = 6t - 6", color=:red, lw=2, title= "Aceleração")
plot!(t, zeros(length(t)), color:black, lw=0.5, label="")


function recebe_tuplas(tupla1,tupla2)
    if tupla1 >= tupla2
        return (tupla1...,tupla2...)
    else
        return (tupla2...,tupla1...)
    end
end

############################################################################################################################

# Function that calculate a quadratic equation
function equacao_segundo_grau(a,b,c)
    if a == 0:
        return 'A equação não é do segundo grau'
    end

    delta = b^2 - 4*a*c
    xv = -b / (2*a)
    yv = -delta / (4*a)

    local raizes
    if delta < 0
        raizes = 'não há raízes reais'
    elseif delta == 0
        x_unico = -b / (2*a)
        raize = (x_unico,)
    else:
        raiz_delta = sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        raizes = (x1,x2)

    end

    return (delta = delta, vertices = (xv,yv), raízes = raizes)

end

################################################################################3

function gargalhada(n::integer)
    return 'ha'^n
end

