using System;

namespace hashCodeBooks
{
    class Program
    {
        static void Main(string[] args)
        {

        }
    }

    class Library
    {
        Book[] setBooks; //Books
        int signUpDays;
        int numberOfScannable;

        Library(Book[] setBooks, int SignUpDays, int numberOfScannable)
        {
            this.setBooks = setBooks;
            this.signUpDays = SignUpDays;
            this.numberOfScannable = numberOfScannable;
        }
               
        Book[] getBook()
        {
            return setBooks;
        }
        int getSignUpDays()
        {
            return signUpDays;
        }
        int getNumberOfScannable()
        {
            return numberOfScannable;
        }
    }

    class Book
    {
        
        int bookID;
        int bookScore;
        Book(int bookID, int score)
        {
            this.bookID = bookID;
            this.bookScore = score;
        }
        int getBookID()
        {
            return bookID;
        }
        int bookScore()
        {
            return bookScore;
        }
    }
}
