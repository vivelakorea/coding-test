def ameba(fn, x1, x2, x3, x4, wait=100, tol=0, alpha=1, gamma=2, rho=0.5, sigma=0.5):
    # fn is function to be minimized(example: lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
    # x1, x2, x3 are initial point (type: tuple. example: (0, 0, 0))
    if not (alpha > 0) or not (gamma > 1) or not (0 < rho and rho <= 0.5):
        raise ValueError('parameter inproperate')
    fn_cache = {}
    import sys
    f1 = f1_tmp = sys.maxsize
    count = 0
    while count < wait:
        f = open('ameba_result.txt', 'a')
        f.write('{0}, {1}\n'.format(str(x1), str(f1)))
        f.close()
        if f1 <= f1_tmp and f1_tmp - f1 <= tol:
            count += 1
        else:
            count = 0
        f1_tmp = f1
        # 1. order
        f1 = fn_cache[x1] if x1 in fn_cache else fn(x1) 
        f2 = fn_cache[x2] if x2 in fn_cache else fn(x2) 
        f3 = fn_cache[x3] if x3 in fn_cache else fn(x3) 
        f4 = fn_cache[x4] if x4 in fn_cache else fn(x4)
        fn_cache[x1], fn_cache[x2], fn_cache[x3], fn_cache[x4] = f1, f2, f3, f4
        pairs = [(x1, f1), (x2, f2), (x3, f3), (x4, f4)]
        pairs.sort(key=lambda pair: pair[1])
        x1, x2, x3, x4 = pairs[0][0], pairs[1][0], pairs[2][0], pairs[3][0]
        f1, f2, f3, f4 = pairs[0][1], pairs[1][1], pairs[2][1], pairs[3][1]

        # 2. calculate centroid xo
        xo = ((x1[0] + x2[0] + x3[0]) / 3, (x1[1] + x2[1] + x3[1]) / 3, (x1[2] + x2[2] + x3[2]) / 3)
        
        xr = (xo[0] + alpha * (xo[0] - x4[0]), xo[1] + alpha * (xo[1] - x4[1]), xo[2] + alpha * (xo[2] - x4[2]))
        fr = fn_cache[xr] if xr in fn_cache else fn(xr)
        fn_cache[xr] = fr

        if fr < f1:
            # 4. expansion
            xe = (xo[0] + gamma * (xr[0] - xo[0]), xo[1] + gamma * (xr[1] - xo[1]), xo[2] + gamma * (xr[2] - xo[2]))
            fe = fn_cache[xe] if xe in fn_cache else fn(xe)
            fn_cache[xe] = fe
            if fe < fr:
                x4, f4 = xe, fe
                continue
            else:
                x4, f4 = xr, fr
                continue
        elif fr >= f3:
            # 5. contraction
            xc = (xo[0] + rho * (x4[0] - xo[0]), xo[1] + rho * (x4[1] - xo[1]), xo[2] + rho * (x4[2] - xo[2]))
            fc = fn_cache[xc] if xc in fn_cache else fn(xc)
            fn_cache[xc] = fc
            if fc < f4:
                x4, f4 = xc, fc
                continue
        else:
            # 3. reflection
            x4, f4 = xr, fr
            continue
        # 6. shrink
        x2 = (x1[0] + sigma * (x2[0] - x1[0]), x1[1] + sigma * (x2[1] - x1[1]), x1[2] + sigma * (x2[2] - x1[2]))
        x3 = (x1[0] + sigma * (x3[0] - x1[0]), x1[1] + sigma * (x3[1] - x1[1]), x1[2] + sigma * (x3[2] - x1[2]))
        x4 = (x1[0] + sigma * (x4[0] - x1[0]), x1[1] + sigma * (x4[1] - x1[1]), x1[2] + sigma * (x4[2] - x1[2]))
    f.close()
    return x1, f1

print(ameba(lambda x: (x[0] - 100) ** 2 + (x[1] - 300) ** 2 + (x[2] - 50) ** 2, (1,1,1), (2,2,2), (2,1,0), (3,4,5), wait=10))

