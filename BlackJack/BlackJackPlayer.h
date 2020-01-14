//
//  BlackJackPlayer.h
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//

#include "Player.h"
#include <vector>
using namespace std;
#ifndef BlackJackPlayer_h
#define BlackJackPlayer_h
class BlackJackPlayer: public Player{               //create blackjackplayer class
private:
    string BJPlayerName;                            //keep track of inputed name
    vector<Card> BJPlayerHand;                      //vector of blackjack players cards
    bool isBusted;                                  //keep track if player has busted or not
    int moneyLeft;                                  //keep track of the players money
    bool turnDone;                  //keep track of if the player finished their turn
    int playersBet;                 //keep track of players bet
    
public:
    BlackJackPlayer();              //default constructor
    BlackJackPlayer(string BJPName, int money);     //copy constructor
    void bet(int num);               //keep track of money that the player has bet
    int getMoneyLeft() const;             //check how much money a player has left
    void winLose(bool tf);                 //check if player won or lost to increase/decrease players money
    string getName() const;                 //return players name
    int getBet() const;                    //return players bet
    
    
    
    
    
    
    
    
    
};


#endif /* BlackJackPlayer_h */
