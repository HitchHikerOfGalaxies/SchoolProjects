using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy_Move : MonoBehaviour {

    public float EnemySpeed = 1;
    public float XMoveDirection;
    private int curHealth = 0;
    private int maxHealth = 100;
    private float stunTime = 0;
    private Transform t;
    private SpriteRenderer sr;

    [HideInInspector]public bool isStunned = false;

    public float distance;
    public float awakeRange;
    public float shootInterval;
    public float bulletSpeed = 100;
    public float bulletCooldown;
    public bool lookingRight = true;

    public GameObject bullet;
    public Animator anim;
    public Transform shootPointLeft, shootPointRight;


    Rigidbody2D rgb2D;
    


	// Use this for initialization
	void Awake () {
        
        rgb2D = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        t = GetComponent<Transform>();
        sr = GetComponent<SpriteRenderer>();

        if (curHealth == 0)
        {
            curHealth = maxHealth;
        }
	}
	
	// Update is called once per frame //Checkpoint to previously working code
	void Update () {

        RaycastHit2D hit = Physics2D.Raycast(transform.position, new Vector2(XMoveDirection, 0)); //used to detect movement taken before switching 
        stunTime -= Time.deltaTime;

        if (!isStunned)
        {
            rgb2D.velocity = new Vector2(XMoveDirection, 0) * EnemySpeed;//starts moving enemy thanks to Vector2 along with RigidBody2D.velocity
        }
        if (stunTime < 0)
        {
            rgb2D.velocity = new Vector2(XMoveDirection, 0) * EnemySpeed;
            isStunned = false;
        }
        if (hit.distance < 0.7f) // hit is the limit and hit.distance is how many ?frames? it'll travel before triggering flip
        {
            Flip();
        }
        if (hit.collider.tag == "Player") //sends a message to player symbolizing loss of health
          {
       //     col.SendMessageUpwards("Damage", dmg);
        }

        if (curHealth <= 0)
        {
            Destroy(gameObject);
            ExpManager.instance.ExpGained(2);
 
        }
        
	}


    void Flip()
    {
        if (XMoveDirection > 0)
        {
            XMoveDirection = -1;
        }else
        {
            XMoveDirection = 1;
        }
    }

    void EnemyMovement()
    {
       
    }
    public void Damage(int damage)
    {
        curHealth -= damage;
      //  gameObject.GetComponent<Animation>().Play //makes object flash red to symbolize loss of health
    }
    public void Hitstun(int stun)
    {
        if (stun == 20) { 
        stunTime += 0.5f;
    }
        if (stun == 10)
        {
            stunTime += 10f;
        }
        isStunned = true;
        rgb2D.velocity = new Vector2(0, 0);
               
        
    }
}
