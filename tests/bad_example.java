// Violation Summary:
// ❌ Class name not in PascalCase
// ❌ print statements used
// ❌ long method (> 50 lines)
// ❌ method name not in camelCase
// ❌ missing Javadoc comments

public class bad_example {
    public static void bad_method() {
        System.out.println("This is a bad practice");

        for (int i = 0; i < 55; i++) {
            System.out.println("Line " + i); // Just to simulate method length
        }
    }
}