package main

import (
	"fmt"
	"image"
	"image/color"
	"image/png"
	"os"
	"sync"
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

	noise := generateNoise(size, scale, octaves, persistence, lacunarity, base)

	saveImage("noise-mp.png", noise)

	end := time.Now()
	fmt.Printf("Time: %s\n", end.Sub(start))
}

func generateNoise(size int, scale, octaves, persistence, lacunarity float64, base int) [][]float64 {
	perlinNoise := perlin.NewPerlin(persistence, lacunarity, int32(octaves), int64(base))

	noise := make([][]float64, size)
	var wg sync.WaitGroup

	for i := 0; i < size; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			noise[i] = make([]float64, size)
			for j := 0; j < size; j++ {
				noise[i][j] = perlinNoise.Noise2D(float64(i)/scale, float64(j)/scale)
			}
		}(i)
	}

	wg.Wait()

	return noise
}

func saveImage(filename string, noise [][]float64) {
	img := image.NewGray(image.Rect(0, 0, len(noise), len(noise[0])))
	for i := range noise {
		for j := range noise[i] {
			value := uint8((noise[i][j] + 1) * 127.5) // Map [-1, 1] to [0, 255]
			img.SetGray(i, j, color.Gray{Y: value})
		}
	}

	f, err := os.Create(filename)
	if err != nil {
		fmt.Println("Error creating image file:", err)
		os.Exit(1)
	}
	defer f.Close()

	err = png.Encode(f, img)
	if err != nil {
		fmt.Println("Error encoding image:", err)
		os.Exit(1)
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
