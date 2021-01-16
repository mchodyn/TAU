import org.apache.commons.lang3.NotImplementedException;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.StringUtils;
import org.joda.time.DateTimeZone;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


public class MockitoWallpaperCalculatorTest {
    private WallpaperCalculator wallpaperCalculator;

    @Before
    public void init() {
        wallpaperCalculator = mock(WallpaperCalculator.class);
        when(wallpaperCalculator.calculate()).thenReturn(15.0);
        when(wallpaperCalculator.calculateInUnit(Unit.M)).thenReturn(12.0);
        when(wallpaperCalculator.calculateInUnit(Unit.KM)).thenReturn(10.0);
    }

    @After
    public void tearDown() {

    }

    @Test
    public void testCalculate() {
        //when
        double result = wallpaperCalculator.calculate();

        //then
        assertEquals(result, 15.0, 0.0);
    }

    @Test
    public void testCalculateInM() {
        //given
        Unit unit = Unit.M;
        //when
        double result = wallpaperCalculator.calculateInUnit(unit);
        //then
        assertEquals(result, 12.0,0.0);
    }

    @Test
    public void testCalculateInKM() {
        //given
        Unit unit = Unit.KM;
        //when
        double result = wallpaperCalculator.calculateInUnit(unit);
        //then
        assertEquals(result, 10.0, 0.0);
    }
}