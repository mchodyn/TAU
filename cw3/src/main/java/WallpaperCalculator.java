import org.apache.commons.lang3.NotImplementedException;

enum Unit {
    CM, M, KM
}

public class WallpaperCalculator {
    private double wallWidth;
    private double wallHeight;
    private double excludedSurface;

    public WallpaperCalculator(double wallWidth, double wallHeight, double excludedSurface) {
        this.wallWidth = wallWidth;
        this.wallHeight = wallHeight;
        this.excludedSurface = excludedSurface;
    }

    public double getWallWidth() {
        return wallWidth;
    }

    public void setWallWidth(double wallWidth) {
        this.wallWidth = wallWidth;
    }

    public double getWallHeight() {
        return wallHeight;
    }

    public void setWallHeight(double wallHeight) {
        this.wallHeight = wallHeight;
    }


    public double getExcludedSurface() {
        return excludedSurface;
    }

    public void setExcludedSurface(double excludedSurface) {
        this.excludedSurface = excludedSurface;
    }

    public double calculate() {
        double wallSurface = this.wallHeight * this.wallWidth;

        if (wallSurface < this.getExcludedSurface()) {

            throw new NotImplementedException("error");
        } else return wallSurface - this.getExcludedSurface();
    }

    public double calculateInUnit(Unit unit) {
        double result = this.calculate();

        switch (unit) {
            case CM:
                return result;
            case M:
                return result / 10000;
            case KM:
                return result / 10000 / 10000;
            default:
                throw new NotImplementedException("error");

        }
    }
}
