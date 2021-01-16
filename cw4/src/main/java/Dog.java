public class Dog {
    private final String name;
    private final Integer age;
    private final Float height;
    private final boolean happy;

    public Dog(String name, Integer age, Float height, boolean happy) {
        this.name = name;
        this.age = age;
        this.height = height;
        this.happy = happy;
    }


    public String getName() {
        return name;
    }

    public Integer getAge() {
        return age;
    }

    public Float getHeight() {
        return height;
    }

    public boolean isHappy() {
        return happy;
    }
}
