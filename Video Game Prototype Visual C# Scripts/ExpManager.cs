using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ExpManager : MonoBehaviour {

    public int curExp = 0;
    public static ExpManager instance;

    private void Awake()
    {
        instance = this;
    }
    
    public void ExpGained(int exp)
    {
        curExp += exp; 
        if (curExp > 4)
        {
            curExp = 0;
        }
    }
}
