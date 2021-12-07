using Plots

# funzione di esempio
g(x) = sin.(x)./x.-0.5

# valori per grafico
x = 0.1:0.03:3
y = g(x)

# inizializzazione estremi
xmin = 0.1
xmax = 3.0
@assert g(xmin)*g(xmax) < 0

# precisione dello zero
delta = 0.01

# inizializzazione grafico
plot(x,y)


plot!([xmin], [0], marker = :hex)
plot!([xmax], [0], marker = :hex)


# ciclo di bisezione
anim = @animate while (xmax - xmin > delta)

    xmed = (xmin + xmax)/2
    println(xmed)
    # visualizzazione grafico
    plot(x,y)
    plot!([xmin], [0], marker = :hex, color = :red)
    plot!([xmax], [0], marker = :hex, color = :blue)
    plot!([xmed], [0], marker = :hex, color = :green)

    # restrizione intervallo
    if g(xmed)*g(xmin) > 0
        global xmin = xmed
    else
        global xmax = xmed
    end
end

# crea gif
gif(anim, fps=2)