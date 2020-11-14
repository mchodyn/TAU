package com.mchodyn;

import org.junit.jupiter.api.Test;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import static org.junit.jupiter.api.Assertions.*;

class WallpaperCalculatorTest {

    @Test
    void calculate() {
        WallpaperCalculator calculator = new WallpaperCalculator(10, 10, 0);
        assertEquals(calculator.calculate(),100,0.0);
    }

    @Test
    void calculateWithHole() {
        WallpaperCalculator calculator = new WallpaperCalculator(10,10,10);
        assertTrue(calculator.calculate() == 90.0);
    }

    @Test
    void exception() {
        WallpaperCalculator calculator = new WallpaperCalculator(1,1,10);
        assertThrows(NotImplementedException.class, calculator::calculate);
    }
}