package main

import (
	"fmt"
	"os"
	"time"

	"github.com/aquilax/go-perlin"
)

func main() {
	if len(os.Args) != 7 {
		fmt.Println("Usage: go run main.go <size> <scale> <octaves> <persistence> <lacunarity> <base>")
		os.Exit(1)
	}

	start := time.Now()

	size := atoi(os.Args[1])
	scale := atof(os.Args[2])
	octaves := atof(os.Args[3])
	persistence := atof(os.Args[4])
	lacunarity := atof(os.Args[5])
	base := atoi(os.Args[6])

	generateNoise(size, scale, octaves, persistence, lacunarity, base)

	end := time.Now()
	fmt.Printf("Time: %s\n", end.Sub(start))
}

func generateNoise(size int, scale, octaves, persistence, lacunarity float64, base int) {
	perlinNoise := perlin.NewPerlin(persistence, lacunarity, int32(octaves), int64(base))

	noise := make([][]float64, size)
	for i := range noise {
		noise[i] = make([]float64, size)
	}

	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			noise[i][j] = perlinNoise.Noise2D(float64(i)/scale, float64(j)/scale)
		}
	}
}

func atoi(s string) int {
	i := 0
	for _, r := range s {
		i = i*10 + int(r-'0')
	}
	return i
}

func atof(s string) float64 {
	f := 0.0
	d := 10.0
	decimal := false
	for _, r := range s {
		if r == '.' {
			decimal = true
			continue
		}
		digit := float64(r - '0')
		if decimal {
			f = f + digit/d
			d *= 10
		} else {
			f = f*10 + digit
		}
	}
	return f
}
