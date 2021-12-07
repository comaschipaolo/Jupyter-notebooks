using Plots

# costanti
msole = 2e30
mterra = 6e24
G = 6.67e-11
AU = 1.5e11
yr = 365*24*3600
vterra = 2*pi*AU/yr

nstep = convert(Int64, 1e6)
dt = 1*yr/nstep

# posizione iniziale
x = 1.0*AU
y = 0.0
# velocità iniziale
vx = 0
vy = vterra/1.0

function accelerazione()
    r = sqrt(x^2 + y^2)
    modulo = G*msole/r^2

    return [-x/r*modulo, -y/r*modulo]
end

function passo_integrazione()
    ax, ay = accelerazione()
    global x, y, vx, vy
    x += vx*dt
    y += vy*dt
    vx += ax*dt
    vy += ay*dt
end

x_plot = []
y_plot = []

for i in 1:nstep
    push!(x_plot, x)
    push!(y_plot, y)
    passo_integrazione()
    if i%300 == 0
        println("$i $(x/AU) $(y/AU)")
    end
end
plot(x_plot, y_plot, aspect_ratio=:equal, xlim = (-1.1*AU, 1.1*AU), ylim = (-1.1*AU, 1.1*AU))

