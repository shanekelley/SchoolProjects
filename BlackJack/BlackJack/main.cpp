//
//  main.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/17/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//
#include "Hand.h"
#include "Deck.h"
#include "Card.h"
#include "Player.h"
#include "BlackJackPlayer.h"
#include "Dealer.h"
#include <vector>
#include <iostream>
using namespace std;

int main() {
    cout << "Welcome to Black Jack" << endl << "Player 1, what is your name? "; // get name and money from palyers
    string name1;
    cin >> name1;
    cout << endl << name1 << ", how much money do you have? ";
    int money1;
    cin >> money1;
    cout << endl << "Welcome to Black Jack" << endl << "Player 2, what is your name? ";
    string name2;
    cin >> name2;
    cout << endl << name2 << ", how much money do you have? ";
    int money2;
    cin >> money2;
    
    BlackJackPlayer player1(name1, money1);     //create blackjack players
    BlackJackPlayer player2(name2, money2);
    
    Deck deck1;             //create a deck
    
    Dealer dealer1;         // create dealer
    
    int timesShuffled = 1;  //increase times shuffled to change order each round
    
    int houseUP = 0;        //keep track of how much house is up
    
    char yn = 'y';
    
    while (yn == 'y' or yn == 'Y'){     //loop while player wants to keep playing
        for (int i = 0; i < timesShuffled; i++) {
            deck1.shuffle();        //shuffle deck
        }
        
        
        cout << "Time for everyone to place their bet!" << endl;        //get bets from players
        cout << "-------------------" << endl;
        cout << player1.getName() << ", how much would you like to bet? ";
        int p1Bet;
        int p2Bet;
        cin >> p1Bet;
        cout << endl << player2.getName() << ", how much would you like to bet? ";
        cin >> p2Bet;
        player1.bet(p1Bet);
        player2.bet(p2Bet);
        
        cout << endl << endl << player1.getName() << " bets $" << p1Bet << endl;    //output bets
        cout << player2.getName() << " bets $" << p2Bet << endl << endl;
        
        
        player1.addCard(deck1.deal());      //deal 2 cards to each player
        player2.addCard(deck1.deal());
        dealer1.addCard(deck1.deal());
        player1.addCard(deck1.deal());
        player2.addCard(deck1.deal());
        dealer1.addCard(deck1.deal());
        
        
        cout << "The initial starting cards are:" << endl << "----------------" << endl;    //Display everyones first hand
        cout << player1.getName() << "'s current hand: [??]" << player1.getSecondCard() << endl;
        cout << player2.getName() << "'s current hand: [??]" << player2.getSecondCard() << endl;
        cout << "Dealer's current hand: [??]" << dealer1.getSecondCard() << endl << endl;
        
        
        
        //player1's turn
        cout << player1.getName() << "'s turn:" << endl;
        cout << "------------------" << endl;
        cout << player1.getName() << "'s current hand: ";
        player1.outputCards();
        cout << " (" << player1.getTotal() << " points)" << endl;
        
        char hitStay1;
        cout << "Would you like to hit? y/n: ";
        cin >> hitStay1;
        while (hitStay1 == 'y' and player1.getIsBusted() == false){      //ask player if they want to hit
            cout << endl << player1.getName() << " chooses to hit." << endl;
            player1.hit(deck1);
            if ( player1.getIsBusted() == true){                        //if player has busted exit turn
                cout << player1.getName() << " has busted." << endl;
                hitStay1 = 'n';
            }else{                                              //if not busted keep asking for hit or stay
                cout << player1.getName() << "'s current hand: ";
                player1.outputCards();
                cout << " (" << player1.getTotal() << " points)" << endl;
                cout << "Would you like to hit? y/n: ";
                cin >> hitStay1;
            };
        };
        cout << player1.getName() <<"'s final hand: ";          //output players final hand
        player1.outputCards();
        
        
        cout << endl << endl;
        //player2's turn
        cout << player2.getName() << "'s turn:" << endl << "------------------" << endl;
        cout << player2.getName() << "'s current hand: ";
        player2.outputCards();
        cout << " (" << player2.getTotal() << " points)" << endl;
        
        char hitStay2;
        cout << "Would you like to hit? y/n: ";
        cin >> hitStay2;
        while (hitStay2 == 'y' and player2.getIsBusted() == false){      //ask player if they want to hit
            cout << endl << player2.getName() << " chooses to hit." << endl;
            player2.hit(deck1);
            if ( player2.getIsBusted() == true){                        //if player has busted exit turn
                cout << player2.getName() << " has busted." << endl;
                hitStay2 = 'n';
            }else{                                              //if not busted keep asking for hit or stay
                cout << player2.getName() << "'s current hand: ";
                player2.outputCards();
                cout << " (" << player2.getTotal() << " points)" << endl;
                cout << "Would you like to hit? y/n: ";
                cin >> hitStay2;
            };
        };
            cout << player1.getName() <<"'s final hand: ";          //output players final hand
            player1.outputCards();
        
        
        cout << endl << endl;
        //dealer's turn
        cout << "Dealer's turn:" << endl << "------------------" << endl;
        cout << "Dealer's current hand: ";
        dealer1.outputCards();
        cout << " (" << dealer1.getTotal() << " points)" << endl;
        
        while (dealer1.getTurnDone() == false){      //check if dealer hits or stays
            dealer1.dealerHit(deck1);
        };
        cout << "Dealer's final hand: ";          //output dealers final hand
        dealer1.outputCards();
        
        
        cout << endl << endl << endl << "Let's see how it turned out:" << endl << "---------------" << endl;    //output bet winnings or losings
        int player1Win;    //keep track if player1 wins(1) loses(0) or pushes(2)
        int player2Win;    //keep track if player2 wins(1) loses(0) or pushes(2)
        bool dealerBusted = false; //keep trackif dealer is busted
        if(dealer1.getIsBusted() == true){  //if dealer is busted check if player is busted
            dealerBusted = true;
            if(player1.getIsBusted() == true){
                player1Win = 0;
            }else{
                player1Win = 1;
            }if (player2.getIsBusted() == true) {
                player2Win = 0;
            }else{
                player2Win = 1;
            }
        }if(dealerBusted == false and player1.getTotal() < dealer1.getTotal()){//check if player has lower total than dealer
            player1Win = 0;
        }if (dealerBusted == false and player2.getTotal() < dealer1.getTotal()){//check if player has lower total than dealer
            player2Win = 0;
        }if(dealerBusted == false and player1.getTotal() == dealer1.getTotal()){//check if player has same total than dealer
            player1Win = 2;
        }if (dealerBusted == false and player2.getTotal() == dealer1.getTotal()){//check if player has same total than dealer
            player2Win = 2;
        }if(dealerBusted == false and player1.getTotal() > dealer1.getTotal()){//check if player has higher total than dealer
            player1Win = 1;
        }if (dealerBusted == false and player2.getTotal() > dealer1.getTotal()){//check if player has higher total than dealer
            player2Win = 1;
        }
        
        if (player1Win == 1) {      //check if player1 wins
            cout << "Yowzah! " << player1.getName() << " wins $" << player1.getBet() << endl;
            player1.winLose(true);
            houseUP -= player1.getBet();
        }if (player1Win == 0) {     //check if player1 loses
            cout << "Ouch! " << player1.getName() << " loses $" << player1.getBet() << endl;
            player1.winLose(false);
            houseUP += player1.getBet();
        }if (player1Win == 2) {     //check if player1 pushes
            cout << "Push! " << player1.getName() << " keeps their $" << player1.getBet() << endl;
        }
        
        if (player2Win == 1) {      //check if player2 wins
            cout << "Yowzah! " << player2.getName() << " wins $" << player2.getBet() << endl;
            player2.winLose(true);
            houseUP -= player2.getBet();
        }if (player2Win == 0) {     //check if player2 loses
            cout << "Ouch! " << player2.getName() << " loses $" << player2.getBet() << endl;
            player1.winLose(false);
            houseUP += player2.getBet();
        }if (player2Win == 2) {     //check if player2 pushes
            cout << "Push! " << player2.getName() << " keeps their $" << player2.getBet() << endl;
        }
        
        cout << "The standings so far:" << endl << "----------------" << endl; //output current money
        cout << player1.getName() << " $" << player1.getMoneyLeft() << endl;
        cout << player2.getName() << " $" << player2.getMoneyLeft() << endl;
        cout << "Dealer is up $" << houseUP << endl <<endl;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        player1.clearHand();        //clear hands for possible new round
        player2.clearHand();
        dealer1.clearHand();
        
        
        deck1.refill();     //refill thee deck
        
        timesShuffled++;
        
        
        cout << "Another round? (y or n): ";    //ask players if they wanna play again
        cin >> yn;
        cout << endl;
    };
    
    
    
    
    return 0;
}

