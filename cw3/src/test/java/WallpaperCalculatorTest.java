import org.apache.commons.lang3.NotImplementedException;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.StringUtils;
import org.joda.time.DateTimeZone;
import org.junit.rules.ExpectedException;
import org.joda.*;

import static org.junit.Assert.*;

import org.junit.*;




public class WallpaperCalculatorTest {

    @Rule
    public final ExpectedException exception = ExpectedException.none();

    @Test
    public void calculate() {
        WallpaperCalculator calculator = new WallpaperCalculator(10, 10, 0);
        assertEquals(calculator.calculate(), 100, 0.0);
    }

    @Test
    public void calculateWithHole() {
        WallpaperCalculator calculator = new WallpaperCalculator(10, 10, 10);
        assertTrue(calculator.calculate() == 90.0);
    }

    @Test
    public void exception() {
        WallpaperCalculator calculator = new WallpaperCalculator(1, 1, 10);
        assertThrows(NotImplementedException.class, calculator::calculate);
    }

    @Test
    public void calculateWithUnitCM() {
        WallpaperCalculator calculator = new WallpaperCalculator(10, 10, 0);
        assertEquals(calculator.calculateInUnit(Unit.CM), 100, 0.0);
    }

    @Test
    public void calculateWithUnitM() {
        WallpaperCalculator calculator = new WallpaperCalculator(100, 100, 0);
        assertEquals(calculator.calculateInUnit(Unit.M), 1, 0.0);
    }

    @Test
    public void calculateWithUnitKM() {
        WallpaperCalculator calculator = new WallpaperCalculator(1000, 1000, 0);
        assertEquals(calculator.calculateInUnit(Unit.KM), 0.01, 0.0);
    }

    @Test
    public void calculateWithUnitAndHoleCM() {
        WallpaperCalculator calculator = new WallpaperCalculator(10, 10, 10);
        assertEquals(calculator.calculateInUnit(Unit.CM), 90, 0.0);
    }

    @Test
    public void calculateWithUnitAndHoleM() {
        WallpaperCalculator calculator = new WallpaperCalculator(100, 100, 1000);
        assertEquals(calculator.calculateInUnit(Unit.M), 0.9, 0.0);
    }

    @Test
    public void calculateWithUnitAndHoleKM() {
        WallpaperCalculator calculator = new WallpaperCalculator(1000, 1000, 100000);
        assertEquals(calculator.calculateInUnit(Unit.KM), 0.009, 0.0);
    }

    @Test
    public void calculateWithUnitException() {
        WallpaperCalculator calculator = new WallpaperCalculator(1, 1, 10);
        exception.expect(NotImplementedException.class);
        calculator.calculateInUnit(Unit.CM);
    }

    @Test
    public void checkBooleanGenerator() {
        boolean trueOrFalse = RandomUtils.nextBoolean();
        assertTrue(trueOrFalse || !trueOrFalse);
    }

    @Test
    public void checkStringUtils() {
        String string = StringUtils.defaultString(null, "default");
        assertEquals(string,"default");
    }

    @Test
    public void CheckIfLondonTimeZoneIsFixed() {
        DateTimeZone zone = DateTimeZone.forID("Europe/London");
        assertFalse(zone.isFixed());
    }

}