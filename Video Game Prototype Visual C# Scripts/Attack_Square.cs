using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Attack_Square : MonoBehaviour {

    public Enemy_Move EnemyAI;

    public bool isLeft = false;

    void Awake()
    {
        EnemyAI = gameObject.GetComponentInParent<Enemy_Move>();
    }

    void OnTriggerStay2D(Collider2D col)
    {
       
        
    }
}
