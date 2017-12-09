"""
Coordinate classes for representing a point in some euclidian space.
"""
import math

class Coord3d:
    """
    Coordinate in 3d space, or a vector direction in 3d space.
    """
    def __init__(self, x_or_coord=0, y=0, z=0):
        if isinstance(x_or_coord, Coord3d):
            self.x = x_or_coord.x
            self.y = x_or_coord.y
            self.z = x_or_coord.z
        else:
            self.x = x_or_coord
            self.y = y
            self.z = z

    def tuple(self, dimensions=3):
        if dimensions == 3:
            return (self.x, self.y, self.z)
        elif dimensions == 2:
            return (self.x, self.y)
        else:
            raise NotImplementedError('cannot return tuple of {0} dimensions '.format(dimensions))

    def scaled(self, factor):
        return Coord3d(
            self.x * factor,
            self.y * factor,
            self.z * factor
        )

    def crossed(self, other):
        """
        Return the cross product of this vector * other. This is useful for finding
        a vector which is perpendicular to both input vectors. (e.g. surface normals)
        """
        return Coord3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def plus(self, other):
        """
        Return the result of self + other
        """
        return Coord3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def minus(self, other):
        """
        Return the result of self - other
        """
        return Coord3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def grow(self, amount):
        """
        Return self with all axis values grown by amount. If an axis value is negative
        the amount will be subtracted, otherwise it will be added.
        """
        return Coord3d(
            0 if self.x == 0 else (
                self.x + amount if self.x > 0 else self.x - amount
            ),
            0 if self.y == 0 else (
                self.y + amount if self.y > 0 else self.y - amount
            ),
            0 if self.z == 0 else (
                self.z + amount if self.z > 0 else self.z - amount
            )
        )

    def times(self, other):
        """
        Return a new Coord3d consisting of each components of self multiplied
        by each components of other
        """
        return Coord3d(self.x * other.x, self.y * other.y, self.z * other.z)

    def over(self, other):
        """
        Return a new Coord3d consisting of each component of self divided by
        each component of other
        """
        return Coord3d(self.x / other.x, self.y / other.y, self.z / other.z)

    def equals(self, other):
        """
        Return true if all components of self are equal to all components of other
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def compliment(self):
        """
        Return the compliment of this vector. (negate all the components)
        """
        return Coord3d(-self.x, -self.y, -self.z)

    def dotted(self, other):
        """
        Return the dot product of this vector and another.
        it is the product of the Euclidean magnitudes of
        the two vectors and the cosine of the angle between them
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def normalized(self):
        if self.x != 0 and self.y != 0 and self.z != 0:
            return self.scaled(1 / self.length())
        return Coord3d(0, 0, 0)

    def length_sqr(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return math.sqrt(self.length_sqr())

"""

    Coord3D GetNormalized() const { Coord3D result=*this;return result.Normalize();}

    void Clamp(CoordUnit maxLength) {//faster way to do this without normalize?
        if (maxLength*maxLength < (x*x+y*y+z*z)) {
            Normalize();
            Scale(maxLength);
        }
    }

    void Clamp(const Coord3D &other) {
        x = ClampCoordUnit(x,other.x);
        y = ClampCoordUnit(y,other.y);
        z = ClampCoordUnit(z,other.z);
    }

    Coord3D GetNormalized() { Coord3D result=*this;return result.Normalize();}

    void Scale(const CoordUnit &scale) {
        x *= scale;
        y *= scale;
        z *= scale;
    }
    CoordUnit GetDistance(const Coord3D &o) const {return sqrt(GetDistanceSqr(o));}
    CoordUnit GetDistanceSqr(const Coord3D &o) const {
        return std::abs(Sqr(x-o.x)+Sqr(y-o.y)+Sqr(z-o.z));
    }
    bool IsValid() const {
        return std::isfinite(x) && std::isfinite(y) && std::isfinite(z);
    }

    CoordUnit GetLengthSqr() const { return x*x+y*y+z*z;}

    CoordUnit GetLength() const { return sqrt(GetLengthSqr()); }

    void SetZero(void) {
        x = 0;
        y = 0;
        z = 0;
    }

    bool CloserThan(const Coord3D &point,const CoordUnit distance) {
        return distance*distance > GetDistanceSqr(point);
    }

    bool IsZero() const { return ((x==0) && (y==0) && (z==0)); };


    Coord3D Mirror(const Coord3D &planeNormal) const {
        Coord3D result = *this;//fixme: allow arbitrary planes
        if (planeNormal.x != 0) {
            result.x = -x;
        }
        if (planeNormal.y != 0) {
            result.y = -y;
        }
        if (planeNormal.z != 0) {
            result.z = -z;
        }
        return result;
    }
    static CoordUnit round(CoordUnit a) {
        if (a > 0) {
            return floor(a+0.555555555555559);
        } else {
            return ceil(a-0.5555555555559);
        }
    }
    Coord3D Granulate(const CoordUnit &stepSize) const {
        return Coord3D(round(x/stepSize)*stepSize,round(y/stepSize)*stepSize,round(z/stepSize)*stepSize);
    }


    union {
        struct {
            CoordUnit x;
            CoordUnit y;
            CoordUnit z;
        };
        CoordUnit vec[LENGTH];
    };
    static CoordUnit ClampCoordUnit(CoordUnit a,CoordUnit clampBy) {
        if (std::abs(a) > std::abs(clampBy)) {
            if (a >= 0) {
                return std::abs(clampBy);
            } else {
                return -std::abs(clampBy);
            }
        }
        return a;
    }
    static Coord3D FromString(const char *strValue) {
        float elements[4];
        memset(&elements,0,sizeof(elements));
        if (strValue) {
            sscanf(strValue,"%f %f %f",&elements[0],&elements[1],&elements[2]);
        }
        return Coord3D(elements[0],elements[1],elements[2]);
    }
    static Coord3D GetRandom(const Coord3D &center,const Coord3D &size) {
        Coord3D result = Coord3D(
            (double)rand()/(double)RAND_MAX,
            (double)rand()/(double)RAND_MAX,
            (double)rand()/(double)RAND_MAX);
        return result.Multiply(size) - (size*0.5)+center;
    }
    static Coord3D GetRandom(const Coord3D &center,const CoordUnit size) {
        Coord3D result = Coord3D(
            ((double)rand()/(double)RAND_MAX)*2-1,
            ((double)rand()/(double)RAND_MAX)*2-1,
            ((double)rand()/(double)RAND_MAX)*2-1);
        result.Clamp(1);
        return (result*size)+center;
    }
    static Coord3D GetSpaced(const int index,const Coord3D &center,const Coord3D &size,const Coord3D &counts) {
        Coord3D stepSize = size.Divide(counts);
        Coord3D result = Coord3D(
            index % (int)counts.x,
            (int)floor(counts.x),
            (int)floor(counts.x)*(int)floor(counts.y)
            );
        if (result.y != 0) {
            result.y = (double)(index/(int)floor(result.y));
        }
        result.y = (double)((int)result.y %(int)floor(counts.y));
        if (result.z != 0) {
            result.z = (double)(index/(int)floor(result.z));
        }
        return result.Multiply(stepSize) - (size*0.5)+center;
    }

    const char *ToString() {
        static char coord3DStr[MAX_COORD3D_STR_LEN];
        snprintf(coord3DStr,MAX_COORD3D_STR_LEN-1,"%.5f,%.5f,%.5f",
            x,y,z);
        return coord3DStr;
    }
    static Coord3D GetInvalid() {
        return Coord3D(std::numeric_limits<CoordUnit>::quiet_NaN(),std::numeric_limits<CoordUnit>::quiet_NaN(),std::numeric_limits<CoordUnit>::quiet_NaN());
    }

    static Coord3D SphereLineIntersection(const Coord3D &center,const CoordUnit &r,const Coord3D &start,const Coord3D &line) {
        CoordUnit r2 = r*r;
        Coord3D lineTo = center-start;
        // not used? Coord3D nlineTo = lineTo.GetNormalized();
        Coord3D nline = line.GetNormalized();
        CoordUnit lineToLength2 = lineTo.GetLengthSqr();
        if (lineToLength2 < r2) {//don't really care if the line starts inside the object (right now)
            return Coord3D::GetInvalid();
        } else {
            CoordUnit arcAngle = lineTo.DotProduct(line)/line.GetLengthSqr();
            //CoordUnit arcAngle = lineTo.DotProduct(nline);
            if (arcAngle < 0) {
                return Coord3D::GetInvalid();
            }
            CoordUnit lineLength2 = line.GetLengthSqr();
            CoordUnit b = (r2 - lineToLength2)/lineLength2  +Sqr(arcAngle);
            if (b > 0) {
                CoordUnit d = arcAngle - sqrt(b);//distance along line
                return start + (nline * d);
            } else {
                return Coord3D::GetInvalid();
            }
        }

    }

    static Coord3D AxisAlignedPlaneLineIntersection(const Coord3D &plane,const Coord3D &start,const Coord3D &line) {
        Coord3D tr_plane(plane-start);//translated to linestart =0
        Coord3D tr_line(line-start);
        CoordUnit d = 0;
        if (plane.x != 0) {
            d = tr_line.x/tr_plane.x;
        } else if (plane.y != 0) {
            d = tr_line.y/tr_plane.y;
        } else if (plane.z != 0) {
             d = tr_line.z/tr_plane.z;
        }
        if ((d >= 0) && (d <= 1)) { //intersection
            return line*d+start;
        } else {
            return Coord3D::GetInvalid();
        }
    }
private:
    static const int MAX_COORD3D_STR_LEN = 100;

};
"""