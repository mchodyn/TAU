import org.junit.Test;
import org.junit.*;
import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;



public class MockitoDogTest {
    private Dog mockedDog;

    @Before
    public void init() {
        mockedDog = mock(Dog.class);
        when(mockedDog.getName()).thenReturn("Reksio");
        when(mockedDog.isHappy()).thenReturn(true);
        when(mockedDog.getAge()).thenReturn(4);
    }

    @After
    public void tearDown() {

    }

    @Test
    public void testDogName() {
        //when
        String name = mockedDog.getName();
        //then
        assertEquals(name, "Reksio");
    }

    @Test
    public void testDogHappiness() {
        //when
        boolean isHappy = mockedDog.isHappy();
        //then
        assertTrue(isHappy);
    }

    @Test
    public void testDogAge() {
        //when
        int age = mockedDog.getAge();
        //then
        assertEquals(age, 4);
    }





}