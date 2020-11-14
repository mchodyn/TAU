package com.mchodyn;

import sun.reflect.generics.reflectiveObjects.NotImplementedException;

public class WallpaperCalculator {
    private double wallWidth;
    private double wallHeight;
    private double excludedSurface;

    public WallpaperCalculator(double wallWidth, double wallHeight, double holes) {
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
        if(wallSurface < this.excludedSurface) {
            throw new NotImplementedException();
        }
        else return wallSurface - excludedSurface;
    }
}
