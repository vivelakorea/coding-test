def ameba(fn, x1, x2, x3, tol, wait, alpha=1, gamma=2, rho=0.5, sigma=0.5):
    # fn is function to be minimized(example: lambda x: x[0] ** 2 + x[1] ** 2)
    # x1, x2, x3 are initial point (type: list. example: [0, 0])
    if not (alpha > 0) or not (gamma > 1) or not (0 < rho and rho <= 0.5):
        raise ValueError('parameter inproperate')
    
    import sys
    f1 = f1_tmp = sys.maxsize
    count = 0
    while count < wait:
        if f1_tmp - f1 < tol:
            count += 1
        else:
            count = 0
        f1_tmp = f1
        # 1. order
        f1, f2, f3 = fn(x1), fn(x2), fn(x3)
        pairs = [(x1, f1), (x2, f2), (x3, f3)]
        pairs.sort(key=lambda pair: pair[1])
        x1, x2, x3 = pairs[0][0], pairs[1][0], pairs[2][0]
        f1, f2, f3 = pairs[0][1], pairs[1][1], pairs[2][1]

        # 2. calculate centroid xo
        xo = [(x1[0] + x2[0]) / 2, (x1[1] + x2[1]) / 2]
        
        xr = [xo[0] + alpha * (xo[0] - x3[0]), xo[1] + alpha * (xo[1] - x3[1])]
        fr = fn(xr)

        if fr < f1:
            # 4. expansion
            xe = [xo[0] + gamma * (xr[0] - xo[0]), xo[1] + gamma * (xr[1] - xo[1])]
            fe = fn(xe)
            if fe < fr:
                x3, f3 = xe, fe
                continue
            else:
                x3, f3 = xr, fr
                continue
        elif fr >= f2:
            # 5. contraction
            xc = [xo[0] + rho * (x3[0] - xo[0]), xo[1] + rho * (x3[1] - xo[1])]
            fc = fn(xc)
            if fc < f3:
                x3, f3 = xc, fc
                continue
        else:
            # 3. reflection
            x3, f3 = xr, fr
            continue
        # 6. shrink
        x2 = [x1[0] + sigma * (x2[0] - x1[0]), x1[1] + sigma * (x2[1] - x1[1])]
        x3 = [x1[0] + sigma * (x3[0] - x1[0]), x1[1] + sigma * (x3[1] - x1[1])]

    return x1, f1

print(ameba(lambda x: (x[0] - 100) ** 2 + (x[1] - 300) ** 2, [1,1], [2,2], [2,1], 0.001, 100))

