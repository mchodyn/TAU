import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;


public class StubDogTest {
    private Dog stubDog;

    @Before
    public void init() {
        stubDog = new Dog("Reksio", 4, 4.2f, true);
    }

    @After
    public void tearDown() {

    }

    @Test
    public void testDogName() {
        //when
        String name = stubDog.getName();
        //then
        assertEquals(name, "Reksio");

    }

    @Test
    public void testDogHappiness() {
        //when
        boolean isHappy = stubDog.isHappy();
        //then
        assertTrue(isHappy);
    }

    @Test
    public void testDogAge() {
        //when
        int age = stubDog.getAge();
        //then
        assertEquals(age, 4);
    }





}